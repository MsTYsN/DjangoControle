from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('client/', views.allClients, name='allclients'),
    path('client/add', views.view_client, name='addclient'),
    path('client/<int:code>', views.getClient, name='getclient'),
    path('client/search/', views.searchClient, name='searchclient'),
    path('operation/<int:numero>', views.operationsClient, name='operationsclient'),
    path('compte/', views.allComptes, name='allcomptes'),
    path('compte/add', views.view_compte, name='addcompte'),
    path('compte/search/', views.searchCompte, name='searchcompte'),
    path('operation/add', views.view_operation, name='addoperation'),
]
