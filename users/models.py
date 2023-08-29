from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.defaultModel import globalModel
import uuid


class User(AbstractUser):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    bi =  models.CharField(max_length=15, blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    data_nascimento =models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to="static/images/users/", blank= True, null=True)
    # password = models.CharField(max_length=128)

    # def save(self, *args, **kwargs):
    #     # Ao salvar o usuário, podemos definir a senha usando 'make_password'
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)


    groups = models.ManyToManyField(
    'auth.Group',
    related_name='auth_users',
    blank=True,
    verbose_name=('groups'),
    help_text=(
        'The groups this user belongs to. A user will get all permissions '
        'granted to each of their groups.'
    )
    )
