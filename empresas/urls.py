from django.urls import path
from .views import *

app_name="Empresa_perfil"

urlpatterns = [
    path('', EmpresaListCreateView.as_view(), name="Empresas_Listar"),
    # path('empresas/localizacao', EmpresaListView.as_view(), name="Empresas_Listar"),
    path('<uuid:pk>', EmpresaUpdateDeleteView.as_view(), name="Empresa_Editar_Criar"),


    path('funcionarios',FuncionariosListView.as_view()),
    path('funcionarios/create', FuncionariosCreateView.as_view(), name="Funcionario-Crud" ),


    path('notificacao/geral/criar/', NotificacaoGeralCreateView.as_view()),
    path('empresa/notificacao/criar/', NotificacaoEmpresaCreateView.as_view()),


    path('documentos', DocumentoListCreateView.as_view()),
    path('documento/<uuid:pk>', DocumnetoUpdateDelete.as_view()),


    path('detalhe', DocumentoEmpresaListCreateView.as_view()),
    path('detalhe/<uuid:pk>', DocumnetoEmpresaUpdateDelete.as_view()),




    
    
]
