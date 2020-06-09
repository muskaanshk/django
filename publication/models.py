from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    year = models.CharField(max_length=100)





   

    def __str__(self):
        return self.title
