
import random
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def send_email(to, subject, template_name, context):
    html_message = render_to_string(template_name, context)
    send_mail(
        subject,
        '',
        EMAIL_HOST_USER,
        [to],
        html_message=html_message,
        fail_silently=False,  # Se definido como True, erros de envio não geram exceções
    )

    print("Email enviado para {}".format(to))

gauth = None  # Variável global para armazenar a autenticação

def authenticate():
    global gauth
    if not gauth:
        gauth = GoogleAuth()
        # Load your client configuration from 'Drive_API_KEY.json'
        gauth.LoadClientConfigFile('./Drive_API_KEY.json')
        gauth.LocalWebserverAuth()
    return gauth

def get_drive_instance():
    gauth = authenticate()
    drive = GoogleDrive(gauth)
    return drive


def get_public_link( nome_da_imagem):

            drive = get_drive_instance()
            file_list = drive.ListFile({'q': f"title = '{nome_da_imagem}'"}).GetList()

            if file_list:
                file = file_list[0]  # Supondo que há apenas um arquivo com o mesmo título
                file.InsertPermission({
                    'type': 'anyone',
                    'value': 'anyone',
                    'role': 'reader'
                })
                public_link = file['alternateLink']
                return public_link
            else:
                return "Arquivo não encontrado no Google Drive"


def generate_random_identifier():
        number =random.randint( 100000,600000)
        codigo = (f'LO{number}')
        return codigo