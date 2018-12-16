from django.urls import path
from estate import views
from .views import *


urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),    
]