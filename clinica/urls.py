from django.urls import path
from . import views

urlpatterns=[
    path('', views.consultas_view, name='consultas_view'),
    path('veterinario/<int:id>/', views.veterinario_view, name='veterinario_view'),
]