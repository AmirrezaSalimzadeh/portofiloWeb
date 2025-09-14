from django.db import models

# Create your models here.
class Quotes(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)