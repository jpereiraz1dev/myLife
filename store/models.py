from django.db import models

choices_category = [
    ("PHYSICAL","Physical"),
    ("PROG","Prog"),
    ("ENGLISH","English"),
    ("COLLEGE","College"),
]

class Product(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    desc = models.TextField(null=False,blank=False)
    price = models.IntegerField()
    public = models.BooleanField(default=True)
    

class Task(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    category = models.CharField(max_length=40,choices=choices_category,blank=False,null=True)
    desc = models.TextField(null=False,blank=False)
    points = models.IntegerField()
    duration = models.TimeField()
    done = models.BooleanField(default=False)

