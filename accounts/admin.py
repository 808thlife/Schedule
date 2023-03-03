from django.contrib import admin

# Register your models here.
#FOR AUTH APP

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User)