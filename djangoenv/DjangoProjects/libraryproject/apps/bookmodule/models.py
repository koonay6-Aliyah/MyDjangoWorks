from django.db import models
from django.utils import timezone

# Create your models here.

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

#lab9 before task
#from django.utils import timezone

from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

    def __str__(self):
        return self.name


class Lab9_Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
