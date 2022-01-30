from django.shortcuts import render, get_object_or_404
from .models import Category, Movie, Country
from django.db.models import Q

# Create your views here.
def home(request):
    search = request.GET.get('search')
    if search:
        movies = Movie.objects.filter(Q(persian_name__contains=search) | Q(name__contains=search))
    else:
        movies = Movie.objects.all().order_by('-id')    
    context = {
        'movies': movies,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }

    return render(request, 'product/home.html', context)

def detail(request, slug):
    context={ 
        'movies': get_object_or_404(Movie, slug=slug),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }
    return render(request, 'product/detail.html', context)

def category(request, slug):
    context={
        'categores': Movie.objects.filter(category__slug=slug).order_by('-id'),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }
    return render(request, 'product/category.html', context)

def country(request, slug):
    context = {
        'country': Movie.objects.filter(country__slug=slug).order_by('-id'),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/country.html', context)

def iranian(request):
    context = {
        'iranian': Movie.objects.filter(making=1).order_by('-id'),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/iranian.html', context)

def foreign(request):
    context = {
        'foreign': Movie.objects.filter(making=2).order_by('-id'),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/foreign.html', context)    

def animation(request):
    context = {
        'animation': Movie.objects.filter(category__title='انیمیشن').order_by('-id'),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/animation.html', context)       