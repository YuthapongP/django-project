from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','age']
    search_fields = ['name']
    # list_filter = ['age']

admin.site.register(User, UserAdmin)
