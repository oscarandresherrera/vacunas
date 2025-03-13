from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_persona, name='registrar_persona'),
    path('buscar-informe/', views.buscar_informe, name='buscar_informe'),
]

