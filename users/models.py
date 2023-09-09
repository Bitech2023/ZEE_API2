from django.db import models
from django.contrib.auth.models import AbstractUser
from empresas.models import EmpresaModel
from django.contrib.auth.hashers import make_password
from utils.defaultModel import globalModel  
import uuid


class NivelModel(globalModel):

    nivel = models.CharField(max_length=125)


class User(AbstractUser):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nivelChoices = [
    ('ADMIN','ADMIN'),
    ('EMPRESARIO','EMPRESARIO'),
    ('NORMAL','NORMAL'),    

    ]
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    bi =  models.CharField(max_length=15, blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    data_nascimento =models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to="imagens/users/", default='imagens/users/user.png', blank=True, null=False)
    # nivelid = models.ForeignKey(NivelModel, on_delete=models.CASCADE, null=True)
    nivel = models.CharField(choices=nivelChoices, max_length=50)

    def __str__(self):
        return self.email
    
class UserEmpresaModel(globalModel):
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


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
