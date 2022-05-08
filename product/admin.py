from django.contrib import admin

from .models import Category, Movie, Country, Poster
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'persian_name', 
        'year', 
        'get_country', 
        'IMDB_score', 
        'director',
        'get_category',
        ]

    

    prepopulated_fields = {'slug': ('name', )}    


admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Poster)
admin.site.register(Movie, MovieAdmin)
