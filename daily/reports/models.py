from django.db import models

class UserPreferences(models.Model):
    def __str__(self):
        return f'{self.email}'
    email = models.EmailField()
    class Categories(models.TextChoices): 
        TECH = 'Tech'
        CRYPTO = "Crypto"
        HEALTH = 'Helth'
    categories = models.fields.CharField(choices=Categories.choices, max_length=10, default='Tech')
    created_at = models.DateTimeField(auto_now_add=True)