from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from .models import Category, Movie, Country, Poster, Artist, Comment
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'persian_name', 
        'type_movie',
        'year', 
        'get_country', 
        'IMDB_score', 
        'director',
        'get_category',
        )
    list_filter = (
        'type_movie',
        'country'
    )
    filter_horizontal = (
                        'category', 
                        'country',
                        'artists',
                        )
    prepopulated_fields = {'slug': ('name', )}    

class CommentAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'created',
                    'active',
                    )

admin.site.register(Country)
admin.site.register(
    Category,
    prepopulated_fields = {'slug': ('title', )}  
    )
admin.site.register(Poster)
admin.site.register(Artist)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Movie, MovieAdmin)
