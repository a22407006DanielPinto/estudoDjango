from django.urls import path
from . import views

urlpatterns=[
    ('', views.consultas_view, name='consultas_view'),
    ('veterinario/<int:id>/', views.veterinario_view, name='veterinario_view'),
]