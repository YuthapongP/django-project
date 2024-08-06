from django import forms
from django.db.models.base import Model
from django_app.models import Movie
from user.models import User

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
    Movie = MovieMultipleChoiceField(
        queryset=Movie.objects.order_by('price'),
        required=True, 
        label='Movie',
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = User
        fields = ['name','email','age','movie']
        labels = {
            'name':'Name',
            'email':'Email',
            'age':'Age',
            'movie':'Movie'
        }
    