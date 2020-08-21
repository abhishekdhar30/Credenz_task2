from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model



class Profile(models.Model) :
    num = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
