from django.contrib import admin
from registration.models import User

class Users(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'password', 'birth_date']
    list_display_links = ['id', 'user_name']
    search_fields =  ['user_name']


admin.site.register(User, Users)        