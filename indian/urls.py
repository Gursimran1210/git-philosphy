from django.urls import path
from . import views

urlpatterns = [

    path('', views.indian, name='india'),
    path('<int:indian_id>/',views.inde,name='inde'),


]
