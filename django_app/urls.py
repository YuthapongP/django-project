from django.urls import path
from django_app import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index),
    path('form', views.form),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('contact', views.contact),
    path('grid', views.grid),
    path('register', views.register),
    path('users', views.get_users),
    # path('login', views.user_login),
# Correct usage
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('user_logout/', auth_views.LogoutView.as_view(next_page='/')),  # Logout view
]
