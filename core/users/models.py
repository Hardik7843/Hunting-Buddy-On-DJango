from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    user_name = models.TextField(unique=True )
    password = models.TextField()