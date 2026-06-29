from django.urls import path
from . import views

urlpatterns=[
    path('', views.torneios_view, name='torneios_view'),
    path('torneio/criar/', views.criar_torneio_view, name='criar_torneio_view'),
    path('torneio/editar/<int:id>/', views.editar_torneio_view, name='editar_torneio_view'),
    path('torneio/apagar/<int:id>/', views.apagar_torneio_view, name='apagar_torneio_view'),
    path('atleta/<int:id>/', views.atleta_view, name='atleta_view'),
]