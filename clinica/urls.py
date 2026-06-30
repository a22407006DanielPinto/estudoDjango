from django.urls import path
from . import views

urlpatterns=[
    path('', views.consultas_view, name='consultas_view'),
    path('consulta/criar/', views.criar_consulta_view, name='criar_consulta_view'),
    path('consulta/editar/<int:id>/', views.editar_consulta_view, name='editar_consulta_view'),
    path('consulta/apagar/<int:id>/', views.apagar_consulta_view, name='apagar_consulta_view'),
    path('veterinario/<int:id>/', views.veterinario_view, name='veterinario_view'),
    path('especialidades/', views.especialidades_view, name='especialidades_view'),
]