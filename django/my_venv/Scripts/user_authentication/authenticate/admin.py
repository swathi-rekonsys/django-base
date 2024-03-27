from django.contrib import admin

# Register your models here.

from authenticate.models import *

admin.site.register(User)
