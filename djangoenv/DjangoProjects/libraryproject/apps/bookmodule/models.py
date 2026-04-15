from django.db import models

# Create your models here.
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title


#lab 8 task6
class Address(models.Model):
    city = models.CharField(max_length=100) # [cite: 17]
    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100) # 
    age = models.IntegerField() # 
    # ربط الطالب بالعنوان كـ Foreign Key 
    address = models.ForeignKey(Address, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name