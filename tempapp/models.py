from django.db import models
from django.db.models import Model

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    content = models.TextField()

# Create your models here.
