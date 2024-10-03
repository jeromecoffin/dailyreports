from django.shortcuts import render, redirect
from reports.form import PreferencesForm

def preferences_view(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preferences = form.save()
            return redirect('success_page', preferences.email) 
    else:
        form = PreferencesForm()

    return render(request, 'reports/preferences_form.html', {'form': form})
