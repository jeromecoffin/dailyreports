from django.shortcuts import render, redirect
from reports.form import PreferencesForm
from reports.models import UserPreferences
from reports.ai import generate_daily_reports

def preferences_view(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            preferences = form.save()
            return redirect('success_page', preferences.id) 
    else:
        form = PreferencesForm()

    return render(request, 'reports/preferences_form.html', {'form': form})

def preference_success(request, id):
   preferences = UserPreferences.objects.get(id=id)
   return render(request,
          'reports/success_page.html',
         {'preferences': preferences})

def trigger_report_generation(request):
    """
    View to trigger daily report generation manually.
    """
    if request.method == 'POST':
        # Call the function to generate reports
        generate_daily_reports()
        return redirect('preferences')  # Redirect to success page or homepage

    return render(request, 'reports/generate.html')