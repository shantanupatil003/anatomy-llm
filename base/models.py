from django.db import models

# Create your models here.
class QueryAPIModel(models.Model):
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
