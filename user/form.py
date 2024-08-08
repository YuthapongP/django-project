from django import forms
from django.db.models.base import Model
from django_app.models import Movie
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MovieMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class UserForm(forms.Form):
    Name = forms.CharField(max_length=50, required=True, label='Name')
    Email = forms.EmailField(max_length=50, required=True, label='Email')
    Age = forms.IntegerField(required=True, label='Age')
    # Movie = forms.ModelChoiceField(
    Movie = MovieMultipleChoiceField(
        queryset=Movie.objects.order_by('price'),
        required=True, 
        label='Movie',
        widget=forms.CheckboxSelectMultiple
    )

class UserModelForm(forms.ModelForm):
    # movie = MovieMultipleChoiceField(
    #     queryset=Movie.objects.order_by('price'),
    #     required=True, 
    #     label='Movie',
    #     widget=forms.CheckboxSelectMultiple
    # )
    # # class Meta:
    #     model = User
    #     fields = ['name','email','age']
    #     labels = {
    #         'name':'Name',
    #         'email':'Email',
    #         'age':'Age',
    #     }
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': "Username",
            'email':'Email',
            'password': 'Password',

        }

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(max_length=50, required=True, label='Username')
    email = forms.EmailField(max_length=60)
    password = forms.CharField(max_length=128)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email','password') 

