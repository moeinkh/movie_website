from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    title = models.CharField(
                'عنوان', 
                max_length=50,
                )

    slug = models.SlugField(
                'اسلاگ', 
                max_length=50,
                )                     

    def __str__(self):
        return self.title

class Country(models.Model):

    class Meta:
        verbose_name = 'کشور تولیده کننده'
        verbose_name_plural = 'کشور های تولیده کننده'

    title = models.CharField(
                'عنوان', 
                max_length=50,
                )

    slug = models.SlugField(
                'اسلاگ', 
                max_length=50,
                )

    def __str__(self):
        return self.title        

class Artist(models.Model):

    class Meta:
        verbose_name = 'هنرمند'
        verbose_name_plural = 'هنرمندان'

    name = models.CharField(
                'اسم هنرمند', 
                max_length=128,
                ) 

    image = models.ImageField(
                'عکس',
                upload_to='artists/',
                blank=True,
                null=True, 
                )

    actor = 1
    director = 2
    profession_choice = (
        (actor,'بازیگر'),
        (director ,'کارگردان'),
    )
    profession = models.IntegerField(
                'حرفه',
                choices=profession_choice
                ) 

    birth = models.CharField(
                'تولد',
                max_length=512,
                )

    description = models.TextField(
                'توضیحات', 
                blank=True,
                null=True, 
                )

    def __str__(self):
        return self.name                                              
    


class Movie(models.Model):

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'

    category = models.ManyToManyField(
                Category, 
                related_name='movies', 
                verbose_name='دسته بندی',
                )

    name = models.CharField(
                'اسم', 
                max_length=100,
                )

    slug = models.SlugField(
                'اسلاگ', 
                max_length=100,
                )

    image = models.ImageField(
                'پوستر فیلم', 
                upload_to='image_movie/',
                )

    persian_name = models.CharField(
                'اسم فارسی', 
                max_length=100,
                )

    year = models.IntegerField(
                'سال تولید',
                )

    country = models.ManyToManyField(
                Country, 
                verbose_name='کشور تولید کننده',
                )

    IMDB_score = models.FloatField(
                'امتیاز IMDB',
                )

    director = models.CharField(
                'کارگردان', 
                max_length=100,
                )

    artists = models.ManyToManyField(
                Artist,
                verbose_name='بازیگران', 
                )

    MovieـSummary = models.TextField(
                'خلاصه فیلم',
                )

    iranian = 1
    foreign = 2
    making_choice = (
        (iranian,'ایرانی'),
        (foreign ,'خارجی'),
    )
    making = models.IntegerField(
                'ساخت', 
                choices=making_choice,
                )

    Cinematic = 1
    serial = 2
    type_movie_choice = (
        (Cinematic,'سینمایی'),
        (serial ,'سریال'),
    )
    type_movie = models.IntegerField(
                'فیلم یا سریال؟', 
                choices=type_movie_choice,
                )

    def get_category(self):
        return "\n".join([i.title for i in self.category.all()])

    get_category.short_description = 'ژانر'  

    def get_country(self):
        return "\n".join([i.title for i in self.country.all()])

    get_country.short_description = 'کشور های تولید کننده'  

    def __str__(self):
        return self.name

class Poster(models.Model):

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    movie = models.ForeignKey(
                Movie,
                on_delete=models.CASCADE, 
                verbose_name='فیلم',
                )

    slide = models.ImageField(
                'پوستر', 
                upload_to='poster/',
                )

    alt = models.CharField(
                'اسم تصویر',
                max_length=128,
                ) 

    def __str__(self):
        return self.alt

class Comment(models.Model):

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    movie = models.ForeignKey(
                Movie,
                on_delete=models.CASCADE, 
                verbose_name='فیلم',
                )
    name = models.CharField(
                'نام و نام خانوادگی', 
                max_length=128,
                )
    email = models.EmailField(
                'ایمیل',
                )              
    text = models.TextField(
                'متن',
                )
    active = models.BooleanField(
                'فعال؟', 
                default=True,
                )  
    created = models.DateTimeField(
                'زمان ایجاد', 
                auto_now_add=True,
                )
    updated = models.DateTimeField(
                'زمان اپدیت', 
                auto_now=True,
                )

    def __str__(self):
        return self.name            