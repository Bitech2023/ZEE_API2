from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [

    #    path('auth/',include('rest_framework.urls', namespace = 'rest_framework')),
    #    path('create/', UserListCreateView.as_view(),name="User-List-Create")
         path('auth/list/', UserListView.as_view(), name="User"),
         path('auth/create/', UserCreateView.as_view(), name="User-Create")

]