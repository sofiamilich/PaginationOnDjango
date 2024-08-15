from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def index(request):
    per_page = request.GET.get('per_page', 2)
    post = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})






# def index(request):
#
#     post = Post.objects.all().order_by('-created_at')
#     paginator = Paginator(post, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#
#     # возвращает функцию render, импортированную по умолчанию в django
#     return render(request, 'index.html', {'page_obj': page_obj})
