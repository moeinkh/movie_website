from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<slug:slug>/', views.detail, name='detail'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('country/<slug:slug>/', views.country, name='country'),
    path('iranian/', views.iranian, name='iranian'),
    path('foreign/', views.foreign, name='foreign'),
    path('animation/', views.animation, name='animation'),
]