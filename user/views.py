from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from user.models import User
from user.form import UserModelForm, UserForm


# Create your views here.

def user(request):
    return HttpResponse("Hello")

def form(request):
    userform = UserForm(request.POST)
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        print(form)
        if form.is_valid:
            form.save()
            
            # user = User()
            # user.name = data['Name']
            # user.email = data['Email']
            # user.age = data['Age']
            # user.save()
            # user.movie.set(data['Movie'])
            return redirect('')
    else:
        form = UserModelForm()
    return render(request, 'regis_form.html', {'userform':userform})

