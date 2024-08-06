from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_app.models import Movie
from django.contrib import messages
import random


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

def grid(request):
    return render(request,'grid.html')
