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

### 6. Email

```
Hello <user>,

Here are your daily AI-generated reports:

Category: Travel

**Airlines Rally to Mitigate Holiday Travel Chaos**
As holiday travel approaches, major airlines are implementing new strategies to minimize delays and cancellations. Airlines like American, Delta, and United are hiring additional staff and boosting flight schedules to accommodate the expected surge in demand. These measures aim to create a smoother experience for travelers as they navigate busy airports during the festive season. (Source: CNN Travel)

**Boost in International Tourism as Borders Reopen**
As countries continue to lift travel restrictions, international tourism is witnessing a robust recovery. Destinations in Europe and Asia are particularly seeing a surge, with travelers eager to explore after years of restrictions. Insights from tourism boards indicate that popular spots are preparing for a record influx of visitors in the coming months. (Source: Travel Weekly)
**Cruise Industry Sets Sail: Record Bookings for 2024**
The cruise industry reports an unprecedented number of bookings for 2024, signaling a strong rebound from the pandemic's impact. Major cruise lines are introducing new itineraries and destinations to attract travelers, reflecting a renewed interest in cruising. This spike is encouraging for the industry, which had previously faced steep declines in passenger numbers. (Source: Bloomberg)

**Sustainable Travel: Popularity of Eco-Friendly Accommodations**
Eco-friendly travel options are gaining traction among conscious travelers as sustainability takes center stage. Various hospitality platforms are highlighting eco-lodges and green hotels that prioritize environmental stewardship while providing unique experiences. This shift is not just a trend but a reflection of changing consumer values in the travel sector. (Source: National Geographic)

**Tech Innovations Transforming Airport Experience**\nAirports are increasingly adopting technology to enhance the travel experience, with innovations such as biometric screening and automated check-in processes. These advancements aim to reduce wait times and streamline passenger flow, improving overall efficiency at airports worldwide. As travel demand continues to recover, these tech solutions are becoming essential for modern air travel. (Source: The Points Guy)

Category: Education

**Schools Embrace AI Tools for Enhanced Learning**
New advancements in artificial intelligence are transforming classrooms as schools across the United States begin integrating AI tools into their curriculums. Educators are using these technologies to personalize learning experiences, automating administrative tasks, and creating interactive environments. Experts believe that embracing AI in education can significantly improve student engagement and outcomes. (Source: EdTech Magazine)

**COVID-19 Vaccination Rates Among Students Surge**
A new report shows that COVID-19 vaccination rates among middle and high school students have increased dramatically in the wake of new federal guidelines. Health officials state that this surge is crucial as schools plan for a full return to in-person learning without restrictions. This increase is seen as a significant step toward protecting students and staff as the pandemic continues to evolve. (Source: The New York Times)

**College Enrollment in Decline: What Does It Mean?**
Recent statistics reveal a continuing decline in college enrollment across the United States, with a notable drop in first-time students. Experts attribute this trend to rising costs, changing job market dynamics, and the impact of the pandemic on student decision-making. Universities are now grappling with strategies to attract more students and adapt to these new challenges. (Source: Inside Higher Ed)

**Debate Heats Up Over School Curriculum Changes**
A contentious debate is underway in various states regarding proposed changes to the school curriculum, focusing on topics such as history and social studies. Proponents argue that updates are necessary to incorporate diverse perspectives, while opponents fear that this may lead to indoctrination. As public hearings are held, the outcome will likely shape the educational landscape for years to come. (Source: NPR)

**Innovative Literacy Programs Gain Momentum**
Several school districts are launching innovative literacy programs aimed at improving reading skills among elementary students. These programs utilize digital resources, community engagement, and family involvement to create a comprehensive approach to literacy education. Early reports indicate promising effects, with some districts seeing significant improvements in student reading levels. (Source: Education Week)

Best regards,
Daily Report AI
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, feel free to open a pull request or an issue for discussion.
