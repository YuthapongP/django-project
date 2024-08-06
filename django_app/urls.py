from django.urls import path
from django_app import views

urlpatterns = [
    path('',views.index),
    path('form', views.form),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('contact', views.contact),
    path('grid', views.grid)
]
