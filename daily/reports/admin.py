from django.contrib import admin

# Register your models here.

from reports.models import UserPreferences

admin.site.register(UserPreferences)