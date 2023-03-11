from django.db import models

# Create your models here.
class Question (models.Model):
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Products (models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to="user-images")
    link = models.URLField(max_length=200)
    publish_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

