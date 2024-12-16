from django.urls import path
from .views import get_admisiones, get_pacientes, get_cias, get_empresas, get_medicos, get_admisiones_seguros, get_liquidaciones, get_facturas, get_devoluciones

urlpatterns = [
    path('admisiones/', get_admisiones, name='get_admisiones'),
    path('admisiones_seguros/', get_admisiones_seguros,
         name='get_admisiones_seguros'),
    path('pacientes/', get_pacientes, name='get_pacientes'),
    path('cias/', get_cias, name='get_cias'),
    path('empresas/', get_empresas, name='get_empresas'),
    path('medicos/', get_medicos, name='get_medicos'),
    path('liquidaciones/', get_liquidaciones, name='get_liquidaciones'),
    path('facturas/', get_facturas, name='get_facturas'),
    path('devoluciones/', get_devoluciones, name='get_devoluciones')
]
