from django.urls import path
from user import views


urlpatterns = [
    path('',views.user),
    path('form', views.form)
]

