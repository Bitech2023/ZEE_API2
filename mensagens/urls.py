from django.urls import path
from .views import *

app_name = "Mensagem"

urlpatterns = [
    path('notificacao/geral/criar/', NotificacaoGeralCreateView.as_view()),
    path('notificacao/empresa/criar/', NotificacaoEmpresaCreateView.as_view())
]