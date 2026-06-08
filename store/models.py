from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    desc = models.TextField(null=False,blank=False)
    price = models.IntegerField()
    public = models.BooleanField(default=True)
    

class Task(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    desc = models.TextField(null=False,blank=False)
    points = models.IntegerField()
    duration = models.TimeField()
    done = models.BooleanField(default=False)

