from django.contrib import admin
from .models import Paciente, Doctor, CitaMedica

# --- CONFIGURACIÓN DEL PANEL DE ADMINISTRACIÓN (BACKEND) ---
# Aquí controlamos cómo se ven y comportan las tablas en /admin/
# Heredamos de admin.ModelAdmin para personalizar la interfaz.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    # list_display: Columnas que se mostrarán en la tabla principal
    list_display = ('nombre', 'apellido', 'edad', 'fecha_nacimiento')
    # search_fields: Permite buscar por estos campos (caja de búsqueda superior)
    search_fields = ('nombre', 'apellido')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad', 'edad')
    search_fields = ('nombre', 'apellido', 'especialidad')
    list_filter = ('especialidad',) # Filtro muy útil para buscar doctores por tipo
@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    # Mostramos nombres relacionados gracias a los def __str__ de los otros modelos
    list_display = ('paciente', 'doctor', 'fecha', 'hora', 'motivo')
    # search_fields: Usamos '__nombre' para buscar dentro de la tabla relacionada (JOIN implícito)
    search_fields = ('paciente__nombre', 'paciente__apellido', 'doctor__nombre', 'doctor__apellido', 'motivo')
    list_filter = ('fecha', 'doctor', 'paciente')
    #Hace que elegir paciente/doctor sea un buscador en lugar de una desplegable eterna al crecer la cantidad de pacientes/doctores
    raw_id_fields = ('paciente', 'doctor')
