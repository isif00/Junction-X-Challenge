import os 
from django.shortcuts import render
from .forms import QuestionForm
from .models import Products
from dotenv import load_dotenv
import openai


load_dotenv()

openai.api_key = os.getenv('API_KEY')


def store(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)

def home(request):
    form = QuestionForm()
    formatted_response = ''
    if request.method == 'POST':
        question = request.POST['question']
        response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=1, max_tokens=1000)
        formatted_response = response['choices'][0]['text']
        print(question)
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'formatted_response': formatted_response,
    }
    return render(request, 'home.html', context)