from django.contrib import admin
from .models import Question, Products


# Register your models here.

admin.site.register(Question)
admin.site.register(Products)