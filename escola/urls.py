from django.urls import path
from . import views

urlpatterns=[
    path('', views.cursos_view, name='cursos_view'),
    path('curso/criar/', views.criar_curso_view, name='criar_curso_view'),
    path('curso/editar/<int:id>/', views.editar_curso_view, name='editar_curso_view'),
    path('curso/apagar/<int:id>/', views.apagar_curso_view, name='apagar_curso_view'),
    path('estudante/<int:id>/', views.estudante_view, name='estudante_view'),
]