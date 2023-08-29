from django.urls import path,include
from .views import *

app_name="Empresa_perfil"

urlpatterns = [
    path('empresa/list/', EmpresaListView.as_view(), name="Empresas_Listar"),
    path('empresa/create/', EmpresaCreateView.as_view(), name="Empresa_Criar"),
    path('empresa/update/<uuid:pk>/', EmpresaUpdateDeleteView.as_view(), name="Empresa_Editar_Criar"),
    path('empresa/<uuid:pk>/funcionarios/', FuncionariosView.as_view(), name="Funcionario-Crud" ),
    

]