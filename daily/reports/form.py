from django import forms

class PreferencesForm(forms.Form):
    email = forms.EmailField()
    categories = forms.MultipleChoiceField(choices=[
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('crypto', 'Cryptocurrency'),
    ], widget=forms.CheckboxSelectMultiple)