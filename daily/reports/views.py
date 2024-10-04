from django.shortcuts import render, redirect
from reports.form import PreferencesForm
from reports.models import UserPreferences, Report
from datetime import datetime
from openai import OpenAI



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

def generate_report(category):
    # Prompt tailored for the specific category
    prompt = f"Give a 5-point daily report on latest news about {category} from the last 24h. Use references from different website. Be precise on the news. For each point, write a catchy title and a paragraph of 3 sentences maximum."

    # Call the ChatGPT API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use appropriate model
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
    )

    # Extract the generated text
    report_text = response.choices[0].message

    return report_text

def generate_daily_reports():

    # Get all unique categories from user preferences
    categories = ['tech', 'crypto', 'health', 'finance', 'sports', 'politics', 'entertainment', 'travel', 'education', 'business', 'science', 'environment', 'fashion', 'gaming', 'art', 'history', 'lifestyle']

    # For each category, generate a report
    for category in categories:
        # Generate report for the current category
        report_text = generate_report(category)
        
        # Save the report to the database
        Report.objects.create(
            category=category,
            report=report_text,
            date=datetime.now()
        )

def trigger_report_generation(request):
    """
    View to trigger daily report generation manually.
    """
    if request.method == 'POST':
        # Call the function to generate reports
        generate_daily_reports()
        return redirect('preferences')  # Redirect to success page or homepage

    return render(request, 'reports/generate.html')