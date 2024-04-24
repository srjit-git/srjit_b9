from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=20)
    author_name=models.CharField(max_length=20)
    rate=models.IntegerField()

class Human(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)