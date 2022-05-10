from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:slug>/', views.detail, name='detail'),
    path('category/<str:slug>/', views.category, name='category'),
    path('country/<str:slug>/', views.country, name='country'),
    path('film/', views.film, name='film'),
    path('series/', views.series, name='series'),
    path('animation/', views.animation, name='animation'),
]