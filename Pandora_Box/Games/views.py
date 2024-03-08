from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 - ceil(n/4 -n//4 )

    params = {"products":products,"nSlides":nSlides,"range":range(1,nSlides)}
    return render(request, 'carouseltest7.html',params)

def about(request):
    return render(request, 'about.html')

def carouseltest7(request):
    return render(request, 'carouseltest7.html')

def community(request):
    return render(request, 'community.html')

def support(request):
    return render(request, 'support.html')

def base(request):
    return render(request, 'base.html')