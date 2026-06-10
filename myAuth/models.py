from django.db import models
from django.contrib.auth.models import AbstractUser

language_options = [
    ("ENGLISH","English"),
    ("PORTUGUESE","Portuguese"),
    ("SPANISH","Spanish"),
    ("RUSSIAN","Russian"),
]

class MyUser(AbstractUser):
    points = models.PositiveIntegerField(null=False,blank=False,default = 500)
    country = models.CharField(max_length=30,null=True,blank=True)
    ddd = models.CharField(max_length=3,null=True,blank=True)
    phone = models.CharField(max_length=9,null=True,blank=True)
    language = models.CharField(choices=language_options,default="ENGLISH",max_length=10)
    

    def __str__(self):
        return f"{self.username}"
