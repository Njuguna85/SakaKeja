from django.urls import path
from estate import views
from .views import *


app_name='estate'

urlpatterns = [ 
    path('', views.indexView.as_view(), name='index'),
    path('about/', views.aboutView.as_view(), name='about'),
]