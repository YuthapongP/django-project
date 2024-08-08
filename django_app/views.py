from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django_app.models import Movie
# from user.form import UserModelForm
from user.form import CustomUserCreationForm
from user.models import User
from django.contrib import messages
import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    title = Movie.objects.all().order_by('-id')
    Random_Number = random.sample(range(1,4000),20)
    return render(request,'about.html', {'title':title, 'Random_Number': Random_Number})

def form(request):
    if request.method == "POST":
        title = request.POST['title']
        price = request.POST['price']
        movie = Movie.objects.create(
            title=title,
            price=price

        )
        movie.save()
        messages.success(request, "Done!")
        print(title, price)
        return redirect("/")
    else:
        return render(request, 'form.html')
    
def edit(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.title = request.POST["title"]
        movie.price = request.POST["price"]
        movie.save()
        return redirect('/')
    else:
        data = Movie.objects.get(id=id)
        return render(request, 'edit.html', {'data':data})


def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    messages.success(request, "Done!")
    return redirect('/')

def contact(request):
    return render(request,'contact.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             # Save the data to the database
#             form.save()
#             # Redirect or render a success page
#             return redirect('/')
#     else:
#         form = UserModelForm()
    
#     return render(request, 'register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('loginz')  # Or your desired redirect
            except IntegrityError:
                form.add_error('username', 'This username is already taken. Please choose a different one.') 
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
def get_users(request):
    users = User.objects.all()  # Retrieve all User objects from the database
    return render(request, 'users.html', {'users': users})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def grid(request):
    return render(request,'grid.html')

