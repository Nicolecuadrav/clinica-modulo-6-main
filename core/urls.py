"""
Módulo de URLs para la aplicación 'core'.
Define las rutas de acceso a las vistas, incluyendo autenticación y gestión de modelos.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import render # Importación necesaria para la vista de prueba de error 404

urlpatterns = [
    # --- Autenticación ---
    # Vista de Login personalizada usando la plantilla 'core/registration/login.html'
    path('login/', auth_views.LoginView.as_view(template_name = 'core/registration/login.html'), name='login'),
    # Vista de Logout que redirige a la raíz ('/') tras cerrar sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # --- Panel de Control Principal ---
    # Vista protegida que sirve como dashboard principal
    path('panel/', views.PanelControlView.as_view(), name='panel_control'),
    
    # --- Gestión de Pacientes (CRUD) ---
    path('pacientes/', views.PacienteListView.as_view(), name='listar_paciente'), # Listado
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='crear_paciente'), # Creación
    path('pacientes/eliminar/<int:pk>/', views.PacienteDeleteView.as_view(), name='eliminar_paciente'), # Eliminación por ID (pk)
    path('pacientes/editar/<int:pk>/', views.PacienteUpdateView.as_view(), name='editar_paciente'),



    # --- Gestión de Doctores (CRUD) ---
    path('doctores/', views.DoctorListView.as_view(), name='listar_doctor'), # Listado
    path('doctores/nuevo/', views.DoctorCreateView.as_view(), name='crear_doctor'), # Creación
    path('doctores/editar/<int:pk>/', views.DoctorUpdateView.as_view(), name='editar_doctor'), # Edición por ID
    path('doctores/eliminar/<int:pk>/', views.DoctorDeleteView.as_view(), name='eliminar_doctor'), # Eliminación por ID

    # --- Gestión de Horas Médicas / Citas (CRUD) ---
    path('horas/', views.CitaListView.as_view(), name='listar_hora'), # Listado
    path('horas/nueva/', views.CitaCreateView.as_view(), name='crear_hora'), # Creación
    path('horas/editar/<int:pk>/', views.CitaUpdateView.as_view(), name='editar_hora'), # Edición por ID
    path('horas/eliminar/<int:pk>/', views.CitaDeleteView.as_view(), name='eliminar_hora'), # Eliminación por ID

    # --- Utilidades y Pruebas ---
    # Ruta temporal para probar visualmente la página de error 404
    path('test-404/', lambda request: render(request, '404.html')),
]
