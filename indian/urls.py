from django.urls import path
from . import views

urlpatterns = [

    path('', views.indian, name='india'),
    path('word/', views.words_list, name='word'),


]
