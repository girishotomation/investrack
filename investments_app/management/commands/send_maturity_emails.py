# your_app/management/commands/send_maturity_emails.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from investments_app.models import Investment
from django.utils import timezone
from django.conf import settings

class Command(BaseCommand):
    help = 'Send maturity notification emails to users'
    """
    def handle(self, *args, **options):
        current_date = timezone.now().date()
        maturing_investments = Investment.objects.filter(date_of_maturity=current_date)
    """
    def handle(self, *args, **options):
        current_date = timezone.now().date()       
        maturing_investments_this_month = Investment.objects.filter(
            date_of_maturity__month=current_date.month,            
        )               
        subject="Your investments maturing this month"
        self.send_emails(maturing_investments_this_month,subject)
        self.stdout.write(self.style.SUCCESS('Emails sent successfully-Monthly'))

        # Emails for investments maturing today
        maturing_investments_today = Investment.objects.filter(date_of_maturity=current_date)
        if current_date :
            subject ="Your Investment is Maturing Today"
            self.send_emails(maturing_investments_today,subject)
            self.stdout.write(self.style.SUCCESS('Emails sent successfully'))

    def send_emails(self, investments, subject):
        for investment in investments:
            self.send_maturity_notification_email(investment,subject)
            self.stdout.write(self.style.SUCCESS(f'Successfully sent email for Investment {investment.investment_id}'))

    def send_maturity_notification_email(self, investment,subject):        
        subject = subject
        if "Today" in subject:
            message = f'Your investment in {investment.financial_institution} of amount {investment.investment_amount} is maturing today, into {investment.crediting_bank_account}.'
        else:
            message = f'Your investment in {investment.financial_institution} of ammount {investment.investment_amount} is maturing this month,on {investment.date_of_maturity}.'
        from_email = settings.DEFAULT_FROM_EMAIL
        #to_email = instance.email
        to_email = [investment.user.email]

        # Use send_mail for simpler cases or use SendGrid API for advanced features
        send_mail(subject, message, from_email, to_email)

        # If you prefer using SendGrid API
        # sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')
        # message = Mail(from_email, to_email, subject, message)
        # sg.send(message)
