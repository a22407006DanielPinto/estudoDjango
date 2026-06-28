from django.urls import path
from . import views

urlpatterns=[
    path('', views.torneios_view, name='torneios_view'),
    path('atleta/<int:id>/', views.atleta_view, name='atleta_view'),
]