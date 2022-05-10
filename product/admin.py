from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
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
admin.site.register(
    Category, 
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields = {'slug': ('title', )}  )
admin.site.register(Poster)
admin.site.register(Movie, MovieAdmin)
