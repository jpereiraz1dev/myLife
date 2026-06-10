from django.db import models
from datetime import timedelta
from myAuth.models import MyUser

class Product(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=20,null=True,blank=False)
    desc = models.TextField(null=False,blank=False)
    price = models.IntegerField()
    public = models.BooleanField(default=True)
    

class CategoryTask(models.Model):
    name = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=20,null=True,blank=False,)
    desc = models.TextField(null=False,blank=False)
    category = models.ForeignKey(CategoryTask,blank=False,null=True, on_delete=models.SET_NULL)
    points = models.IntegerField()
    duration = models.TimeField(default = timedelta(minutes=30))
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

