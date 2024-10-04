from django.contrib import admin

# Register your models here.

from reports.models import UserPreferences, Report

admin.site.register(UserPreferences)
admin.site.register(Report)