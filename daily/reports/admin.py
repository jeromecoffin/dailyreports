from django.contrib import admin
from reports.models import UserPreferences, Report

class ReportAdmin(admin.ModelAdmin):  
    list_display = ('date', 'category')

admin.site.register(UserPreferences)
admin.site.register(Report, ReportAdmin)