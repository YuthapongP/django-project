from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','password']
    search_fields = ['username']
    # list_filter = ['age']

admin.site.register(User, UserAdmin)
