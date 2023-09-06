from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [



         path('', UserListCreateView.as_view()),
         path('<uuid:pk>',UserRetrieveView.as_view(), name="User-List-One"),
        #  path('create/', UserCreateView.as_view(), name="User-Criar"),
         path('update/<uuid:pk>', UserUpdateDelete.as_view(), name='usuario-retrieve-update-destroy'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)