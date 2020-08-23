from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class ShortUrl(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(max_length=8, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)