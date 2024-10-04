# Daily Report Generator - Django Application

This Django application allows users to select categories of interest (e.g., tech, crypto, health, etc.) and receive daily synthetic reports generated using OpenAI's GPT-4 API. The reports are generated once per day for each category, and users receive a summary of 5 key points on each chosen topic via email.

## Features

- **User Preferences**: Users can select their preferred categories and provide their email address via a form.
- **Daily Report Generation**: A report is generated every morning for each category using OpenAI's GPT API.
- **Manual Trigger**: Admins can manually trigger the report generation process from a web interface.
- **Success Confirmation**: After submitting preferences, users are redirected to a success page that confirms their selections.

## Requirements

- Python 3.8+
- Django 3.2+
- OpenAI Python package (>=1.0.0)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/daily-report-generator.git
cd dailyreports
```

### 2. Install Dependencies

Ensure you have Python 3 and pip installed. Then install the necessary dependencies:

```bash
pip install -r requirements.txt
```

In the `requirements.txt`, make sure the following packages are included:

```
Django>=3.2
openai>=1.0.0
```

### 3. Configure OpenAI API

Create an `.env` file or use any configuration manager to set your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key
```

### 4. Set up Django Database

Run migrations to create the necessary database schema:

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

If you want to access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, navigate to `http://127.0.0.1:8000/` in your browser to see the application.

## Application Structure

### 1. Models

This application uses two main models:

- **UserPreferences**: Stores user preferences for categories and email.
- **Report**: Stores the reports generated for each category.

### 2. Views

- **`preferences_view`**: Handles the display and processing of the preferences form.
- **`preference_success`**: Displays the success message after preferences are saved.
- **`trigger_report_generation`**: Allows manual triggering of the report generation process.

### 3. Templates

- **`preferences_form.html`**: Displays the form where users can select their preferred categories.
- **`success_page.html`**: Displays a confirmation after the user has successfully submitted their preferences.
- **`generate.html`**: Allows admins to manually trigger report generation.

### 4. Forms

The `PreferencesForm` is a Django ModelForm that captures user preferences.

### 5. AI Integration

The `generate_daily_reports` function uses the OpenAI API to fetch a summary for each selected category, which is stored in the `Report` model. The OpenAI API call is made via the new `ChatCompletion.create` method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, feel free to open a pull request or an issue for discussion.
