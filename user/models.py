from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=False, default='')
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    movie = models.ManyToManyField('django_app.Movie')

    def __str__(self):
        return self.name