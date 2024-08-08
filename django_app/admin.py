from django.contrib import admin
from django_app.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    search_fields = ['title']
    # list_filter = ['age']
    
admin.site.register(Movie, MovieAdmin)