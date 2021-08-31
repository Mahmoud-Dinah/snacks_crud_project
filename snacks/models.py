from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Snack (models.Model):
    title = models.CharField(max_length= 256)
    purchaser  = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)

def __str__(self):
    return self.title
