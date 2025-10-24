from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('base/', views.base, name='home'),
    path('contact/', views.contact, name='home'),
    path('game/', views.game, name='home'),
    path('story/', views.story, name='home'),
    path('joke/', views.joke, name='home'),
    path('motivation/', views.motivation, name='home'),
    path('telegram/', views.telegram, name='home'),
    path('reasoning/', views.reasoning, name='home'),
]