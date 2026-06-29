from django.urls import path
from . import views

urlpatterns=[
    path('', views.receitas_view, name='receitas_view'),
    path('receita/criar/', views.criar_receita_view, name='criar_receita_view'),
    path('receita/editar/<int:id>/', views.editar_receita_view, name='editar_receita_view'),
    path('receita/apagar/<int:id>/', views.apagar_receita_view, name='apagar_receita_view'),
    path('utilizador/<int:id>/', views.utilizador_view, name='utilizador_view'),
]