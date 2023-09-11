from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [


         path('', UserListCreateView.as_view()),
         path('<uuid:pk>',UserRetrieveView.as_view(), name="User-List-One"),
        #  path('create/', UserCreateView.as_view(), name="User-Criar"),
         path('update/<uuid:pk>', UserUpdateDelete.as_view(), name='usuario-retrieve-update-destroy'),
         path('empresa', USerEmpresaListCreate.as_view(), name="User_Empresa_list_Create"),
         path('empresa/<uuid:pk>', UserEmpresaRetrieveView.as_view()),
         path('empresa/update/<uuid:pk>', UserEmpresaUpdateDelete.as_view(), name="User_update_Delete"),


        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)