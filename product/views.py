from django.shortcuts import render, get_object_or_404
from .models import Category, Movie, Country, Poster
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    search = request.GET.get('search')
    if search:
        movies = Movie.objects.filter(Q(persian_name__contains=search) | Q(name__contains=search))
    else:
        movies = Movie.objects.all().order_by('-id')    

    paginator = Paginator(movies, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config        
    context = {
        'movies': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
        'posters': Poster.objects.all(),
    }
    return render(request, 'product/home.html', context)

def detail(request, slug):
    context={ 
        'movies': get_object_or_404(Movie, slug=slug),
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }
    return render(request, 'product/detail.html', context)

def category_cinematic(request, slug):    
    categories = Movie.objects.filter(category__slug=slug, type_movie=1).order_by('-id')

    paginator = Paginator(categories, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context={
        'categores': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }
    return render(request, 'product/category_cinematic.html', context)

def category_serial(request, slug):    
    categories = Movie.objects.filter(category__slug=slug, type_movie=2).order_by('-id')

    paginator = Paginator(categories, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context={
        'categores': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }
    return render(request, 'product/category_serial.html', context)

def country_cinematic(request, slug):
    country = Movie.objects.filter(country__slug=slug, type_movie=1).order_by('-id')

    paginator = Paginator(country, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context = {
        'country': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/country_cinematic.html', context)

def country_serial(request, slug):
    country = Movie.objects.filter(country__slug=slug, type_movie=2).order_by('-id')

    paginator = Paginator(country, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context = {
        'country': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/country_serial.html', context)

def film(request):
    film = Movie.objects.filter(type_movie=1).order_by('-id')

    paginator = Paginator(film, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context = {
        'film': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/film.html', context)

def series(request):
    series = Movie.objects.filter(type_movie=2).order_by('-id')

    paginator = Paginator(series, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context = {
        'series': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/series.html', context)    

def animation(request):
    animation = Movie.objects.filter(category__title='انیمیشن').order_by('-id')

    paginator = Paginator(animation, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config 
    context = {
        'animation': page_obj,
        'category': Category.objects.all(),
        'countres': Country.objects.all(),
    }    
    return render(request, 'product/animation.html', context)       