from django.urls import path , include
from app import views
from users.views import login , register

urlpatterns = [
    # path('show/' , views.show , name = 'show'),
    path('' , views.index , name='index'),
    
    # users login and register
    path('user/' , include('users.urls')),
    
]