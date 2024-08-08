from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
class User(models.Model):
    username = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=60, default='')
    password = models.CharField(max_length=128, default='')
    # movie = models.ManyToManyField('django_app.Movie')


    def __str__(self):
        return self.name

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username