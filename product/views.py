from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Movie, Country, Poster, Comment
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import MovieFormSearch, CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    search_form = MovieFormSearch(request.GET)
    movies = Movie.objects.all().order_by('-id')  
    search = request.GET.get('search')
    if search:
        movies = Movie.objects.filter(Q(persian_name__contains=search) | Q(name__contains=search))

    if search_form.is_valid():
        if search_form.cleaned_data['category'] is not None:
            movies = movies.filter(category=search_form.cleaned_data['category'])
        if search_form.cleaned_data['country'] is not None:
            movies = movies.filter(country=search_form.cleaned_data['country']) 
        if search_form.cleaned_data['director'] is not None: 
            movies = movies.filter(director__contains=search_form.cleaned_data['director'])
        if search_form.cleaned_data['type_movie'] is not None: 
            movies = movies.filter(type_movie=search_form.cleaned_data['type_movie'])
        if search_form.cleaned_data['artist'] is not None:
            movies = movies.filter(artists__name__contains=search_form.cleaned_data['artist']).distinct()      
    # start pagination config
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
        'search_form': search_form,
    }
    return render(request, 'product/home.html', context)

def detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment()
            comment.movie = movie
            comment.name = comment_form.cleaned_data['name']
            comment.email = comment_form.cleaned_data['email']
            comment.text = comment_form.cleaned_data['text']
            comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
            return redirect(url)
    else:
        comment_form = CommentForm() 
        context={ 
            'movies': movie,
            'category': Category.objects.all(),
            'countres': Country.objects.all(),
            'comment_form': comment_form,
            'comments': Comment.objects.filter(movie=movie, active=True).order_by('-created')
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