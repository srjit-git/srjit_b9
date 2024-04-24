from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name=models.CharField(max_length=20)

class Student(models.Model):
   dept_id=models.ForeignKey(Department,on_delete=models.CASCADE)
   first_name=models.CharField(max_length=20)
   last_name=models.CharField(max_length=20)
   email=models.EmailField()
   phone=models.BigIntegerField()
   pic=models.ImageField(
       upload_to='images/'
   )
