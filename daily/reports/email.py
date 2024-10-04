from django.core.mail import send_mail
from django.conf import settings
from reports.models import UserPreferences, Report
from django.utils import timezone

def send_daily_report_emails():
    """
    This function sends an email to each user with their preferred category reports.
    """
    users = UserPreferences.objects.all()

    # Get today's date to fetch the latest reports
    today = timezone.now().date()

    for user in users:
        # List to store reports for this user
        reports_to_send = []

        # Check user preferences and fetch the reports for each category
        if user.tech:
            reports_to_send.append(get_report_for_category('tech', today))
        if user.crypto:
            reports_to_send.append(get_report_for_category('crypto', today))
        if user.health:
            reports_to_send.append(get_report_for_category('health', today))
        if user.finance:
            reports_to_send.append(get_report_for_category('finance', today))
        if user.sports:
            reports_to_send.append(get_report_for_category('sports', today))
        if user.politics:
            reports_to_send.append(get_report_for_category('politics', today))
        if user.entertainment:
            reports_to_send.append(get_report_for_category('entertainment', today))
        if user.travel:
            reports_to_send.append(get_report_for_category('travel', today))
        if user.education:
            reports_to_send.append(get_report_for_category('education', today))
        if user.business:
            reports_to_send.append(get_report_for_category('business', today))
        if user.science:
            reports_to_send.append(get_report_for_category('science', today))
        if user.environment:
            reports_to_send.append(get_report_for_category('environment', today))
        if user.fashion:
            reports_to_send.append(get_report_for_category('fashion', today))
        if user.gaming:
            reports_to_send.append(get_report_for_category('gaming', today))
        if user.art:
            reports_to_send.append(get_report_for_category('art', today))
        if user.history:
            reports_to_send.append(get_report_for_category('history', today))
        if user.lifestyle:
            reports_to_send.append(get_report_for_category('lifestyle', today))

        # Filter out empty reports
        reports_to_send = [report for report in reports_to_send if report]

        if reports_to_send:
            # Format email content
            email_content = format_email_content(user, reports_to_send)

            # Send the email
            send_mail(
                subject="Your Daily AI-Generated Reports",
                message=email_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )


def get_report_for_category(category, date):
    """
    Fetch the latest report for a specific category and date.
    """
    report = Report.objects.filter(category=category, date__date=date).first()
    if report:
        return f"Category: {category.capitalize()}\n{report.report}\n"
    return None


def format_email_content(user, reports):
    """
    Format the email content for a user by combining all reports.
    """
    email_body = f"Hello {user.email},\n\nHere are your daily AI-generated reports:\n\n"
    for report in reports:
        email_body += report + "\n"  # Add each report to the email content
    
    email_body += "\nBest regards,\nDaily Report AI"
    return email_body
