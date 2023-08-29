from django.urls import path,include 
from .views import *
urlpatterns=[
    

      
      path('' , PerfilListView.as_view()),
      path('create/',ImpostoListCreateView.as_view())



]
