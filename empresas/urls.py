from django.urls import path
from .views import *

app_name="Empresa_perfil"

urlpatterns = [
    path('empresas', EmpresaListView.as_view(), name="Empresas_Listar"),
    path('empresas/localizacao', EmpresaListView.as_view(), name="Empresas_Listar"),
    path('empresa/<uuid:pk>/', EmpresaRetrieveView.as_view(), name="Empresa_List_one"),
    path('empresa/create', EmpresaCreateView.as_view(), name="Empresa_Criar"),
    path('empresas/update/<uuid:pk>', EmpresaUpdateDeleteView.as_view(), name="Empresa_Editar_Criar"),


    path('empresa/funcionarios',FuncionariosListView.as_view()),
    path('empres/funcionarios/create', FuncionariosCreateView.as_view(), name="Funcionario-Crud" ),


    path('notificacao/geral/criar/', NotificacaoGeralCreateView.as_view()),
    path('empresa/notificacao/criar/', NotificacaoEmpresaCreateView.as_view()),


    path('empresa/documentos', DocumentoListCreateView.as_view()),
    path('empresa/documento/<uuid:pk>', DocumnetoUpdateDelete.as_view()),


    path('empresa/detalhe', DocumentoEmpresaListCreateView.as_view()),
    path('empresa/detalhe/<uuid:pk>', DocumnetoEmpresaUpdateDelete.as_view())
    
    
]
