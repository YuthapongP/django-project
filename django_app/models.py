from django.db import models

class Movie(models.Model):
    title = models.CharField(unique=True, max_length=100)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()

    # def __str__(self):
    #     return self.title
