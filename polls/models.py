from django.db import models

# Create your models here.
class Quotes(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # new field
    featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True,null=True)         # new field

    def __str__(self):
        return f'"{self.content}" by {self.author}'