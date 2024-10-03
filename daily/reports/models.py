from django.db import models

class UserPreferences(models.Model):
    def __str__(self):
        return f'{self.email}'
    email = models.EmailField()
    tech = models.fields.BooleanField(default=False)
    crypto = models.fields.BooleanField(default=False)
    health = models.fields.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)