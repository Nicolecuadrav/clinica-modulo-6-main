#!/usr/bin/env python
"""Utilidad de línea de comandos para tareas administrativas de Django."""
import os
import sys


def main():
    """Ejecuta tareas administrativas."""
    # Establece la variable de entorno para indicar a Django dónde encontrar la configuración del proyecto.
    # 'clinica.settings' apunta al archivo settings.py dentro de la carpeta 'clinica'.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinica.settings')
    try:
        # Intenta importar la función que ejecuta los comandos de Django desde la terminal.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si falla la importación, lanza un error claro indicando posibles causas (entorno virtual no activado).
        raise ImportError(
            "No se pudo importar Django. ¿Seguro que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste "
            "activar el entorno virtual?"
        ) from exc
    
    # Ejecuta el comando pasado por terminal (ej: 'runserver', 'migrate', 'createsuperuser').
    # sys.argv contiene los argumentos de la línea de comandos.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Si este script se ejecuta directamente (no importado), llama a la función main().
    main()
