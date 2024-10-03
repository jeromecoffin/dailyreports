from django import forms
from reports.models import UserPreferences

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = '__all__'
