from django.shortcuts import render, redirect
from reports.form import PreferencesForm
import openai

openai.api_key = "your-openai-api-key"

def generate_report(categories):
    prompt = f"Give a 5-point daily report on {', '.join(categories)}."
    response = openai.Completion.create(
        engine="gpt-4",  # Choose the GPT model
        prompt=prompt,
        max_tokens=300,
    )
    return response.choices[0].text.strip()


def preferences_view(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            # Save user preferences or perform necessary actions
            # Redirect or show success message after submission
            return redirect('success_page') 
    else:
        form = PreferencesForm()

    return render(request, 'reports/preferences_form.html', {'form': form})
