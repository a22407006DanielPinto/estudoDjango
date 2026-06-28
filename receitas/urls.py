from django.urls import path
from . import views

urlpatterns=[
    path('', views.receitas_view, name='receitas_view'),
    path('utilizador/<int:id>/', views.utilizador_view, name='utilizador_view'),
]