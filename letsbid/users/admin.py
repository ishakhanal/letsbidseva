from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Usermessage,  Notification

admin.site.register(Profile)
admin.site.register(Usermessage)
admin.site.register(Notification)
