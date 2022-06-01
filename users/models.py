from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = 'users'
    
    cat_name = models.CharField(max_length=256, default='')