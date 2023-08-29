
from django.core.mail import send_mail
from ..config.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

def send_email(to, subject, template_name, context):
    html_message = render_to_string(template_name, context)
    send_mail(
        subject,
        '',
        EMAIL_HOST_USER,
        [to],
        html_message=html_message,
    )
    print("Email enviado para {}".format(to))

#exemplo de uso

send_mail(
    
)