from django.urls import path
from .views import get_admisiones, get_pacientes, get_cias, get_empresas, get_medicos

urlpatterns = [
    path('admisiones/', get_admisiones, name='get_admisiones'),
    path('pacientes/', get_pacientes, name='get_pacientes'),
    path('cias/', get_cias, name='get_cias'),
    path('empresas/', get_empresas, name='get_empresas'),
    path('medicos/', get_medicos, name='get_medicos'),
]
