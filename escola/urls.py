from django.urls import path
from . import views

urlpatterns=[
    path('', views.cursos_view, name='cursos_view'),
    path('estudante/<int:id>/', views.estudante_view, name='estudante_view'),
]