from django.urls import path
from . import views

urlpatterns = [
    path('', views.listeComptes, name='allcomptes'),
    path('client/', views.listeClients, name='allclients'),
    path('client/<int:code>', views.getClient, name='getclient'),
    path('client/search/', views.searchClient, name='searchclient'),
    path('operation/<int:numero>', views.listeOperationsClient, name='getoperationclient'),
    path('client/add', views.view_client, name='addclient'),
    path('compte/add', views.view_compte, name='addcompte'),
    path('operation/add', views.view_operation, name='addoperation'),
]
