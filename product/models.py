from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    parent = TreeForeignKey(
                            'self', 
                            on_delete=models.CASCADE, 
                            related_name='children',
                            null=True, 
                            blank=True, 
                            verbose_name='زیر دسته',
                            )    

    title = models.CharField(
                            'عنوان', 
                            max_length=50,
                            )

    slug = models.SlugField(
                            'اسلاگ', 
                            max_length=50,
                            )

    class MPTTMeta:
        order_insertion_by = ['title']                        

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
                            upload_to='poster/',
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

    stars = models.CharField(
                            'ستارگان', 
                            max_length=300,
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
                                upload_to='poster/sliders',
                                )

    alt = models.CharField(
                            'اسم تصویر',
                            max_length=128,
                            ) 

    def __str__(self):
        return self.alt
