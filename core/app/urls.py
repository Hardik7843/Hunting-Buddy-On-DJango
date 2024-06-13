from django.urls import path
from app import views

urlpatterns = [
    path('show/' , views.show , name = 'show'),
    path('' , views.index , name='index')
]