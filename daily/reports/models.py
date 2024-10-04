from django.db import models

class UserPreferences(models.Model):
    def __str__(self):
        return f'{self.email}'
    
    email = models.EmailField()

    tech = models.fields.BooleanField(default=False)
    crypto = models.fields.BooleanField(default=False)
    health = models.fields.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    politics = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)
    travel = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    science = models.BooleanField(default=False)
    environment = models.BooleanField(default=False)
    fashion = models.BooleanField(default=False)
    gaming = models.BooleanField(default=False)
    art = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    lifestyle = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    category = models.fields.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    report = models.fields.CharField(max_length=1000, default='')

