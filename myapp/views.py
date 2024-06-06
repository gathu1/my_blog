from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    blogs = [
        {'title': 'Learning django', 'content': 'Django is an awesome open source framework for building APIs using Django REST framework.', 'author': 'John Doe', 'date': '2024-6-4'},
        {'title': 'Learning django', 'content': 'Django is an awesome open source framework for building APIs using Django REST framework.', 'author': 'John Doe', 'date': '2024-6-4'},
        {'title': 'Learning django', 'content': 'Django is an awesome open source framework for building APIs using Django REST framework.', 'author': 'John Doe', 'date': '2024-6-4'},

    ]

    context = {'blogs': blogs}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)