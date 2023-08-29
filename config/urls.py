from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from django.urls import path,include
from config import settings
from django.conf.urls.static import static

from lotes.views import *
urlpatterns = [
    path('admin/',    admin.site.urls),
    path("index/"    ,Index.as_view(),name="index"),
    path('api/auth/', TokenObtainPairView.as_view()),
    path('api/', include("lotes.urls")),
    path('api/', include("empresas.urls")),
    path('api/', include("pagamentos.urls")),
    path('api/', include("users.urls")),
 

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
