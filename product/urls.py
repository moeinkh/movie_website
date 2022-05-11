from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:slug>/', views.detail, name='detail'),
    path('cinematic/<str:slug>/', views.category_cinematic, name='category_cinematic'),
    path('serial/<str:slug>/', views.category_serial, name='category_serial'),
    path('country/cinematic/<str:slug>/', views.country_cinematic, name='country_cinematic'),
    path('country/serial/<str:slug>/', views.country_serial, name='country_serial'),
    path('film/', views.film, name='film'),
    path('series/', views.series, name='series'),
    path('animation/', views.animation, name='animation'),
]