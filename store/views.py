from django.shortcuts import render
from .models import Product,Task

def store_page(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request,'store_page.html',context)

def task_list(request):
    tasks = Task.objects.all()
    context = {
        "tasks":tasks
    }
    return render(request,'task_list.html',context)