from django.db import models

class UserPreferences(models.Model):
    email = models.EmailField()
    categories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)