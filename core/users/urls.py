from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login_page , name='loginDirect' ),
    path('login/' , views.login_page , name = 'login'),
    path('registration/' , views.register , name='register')
]