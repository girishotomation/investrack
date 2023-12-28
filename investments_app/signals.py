# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail,TemplateId

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Your Website'
        template_id = 'd-4ea0cc93323348969058a21b4d9f5bfb'        
        message = 'Thank you for registering with us!'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = instance.email

        # Create a SendGrid message
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            #template_id=TemplateId(template_id)
            #plain_text_content=message
        )

        message.template_id=template_id
        """
          message.dynamic_template_data = {
            'username': instance.username,
            'custom_message': 'Thank you for joining!',
        }
        """
        try:
            sg = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
