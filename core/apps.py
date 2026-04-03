from django.apps import AppConfig

# --- CONFIGURACIÓN DE LA APLICACIÓN 'CORE' ---
# Este archivo define los metadatos de esta app particular.
# Se usa principalmente para:
# - Definir el nombre legible en el admin
# - Configurar señales (signals) al inicio

class CoreConfig(AppConfig):
    # Tipo de campo PK por defecto para los modelos de esta app (BigInt)
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core' # Nombre técnico de la app (coincide con la carpeta)
    verbose_name = 'Gestión Clínica' # Nombre visible en el panel de admin
