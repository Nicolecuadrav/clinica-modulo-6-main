# Clínica VitalCare

Sistema de gestión para una clínica médica desarrollado con Django. Permite administrar pacientes, doctores y citas médicas a través de un panel de control protegido por autenticación.

## Funcionalidades

- **Pacientes:** registro, edición, eliminación y listado con búsqueda por nombre. Edad calculada automáticamente.
- **Doctores:** CRUD completo con especialidad médica y búsqueda por nombre.
- **Citas Médicas:** agendamiento con validación de horarios (sin solapamiento para paciente ni doctor) y filtros por fecha y nombre de paciente.
- **Panel de administración** Django con búsqueda y filtros configurados.
- **Autenticación:** login/logout requerido para acceder a todas las vistas.

## Tecnologías

| Componente             | Tecnología            |
| ---------------------- | --------------------- |
| Backend                | Django 5.2.12         |
| Base de datos          | PostgreSQL            |
| Frontend               | Bootstrap 5.3.2 (CDN) |
| Hashing de contraseñas | BCryptSHA256          |
| Variables de entorno   | django-environ        |

## Requisitos previos

- Python 3.10+
- PostgreSQL en ejecución
- pip

## Instalación

```bash
# 1. Clonar el repositorio
git clone git@github.com:Nicolecuadrav/clinica-modulo-6-main.git
cd evaluacion_6

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env y completar DB_PASSWORD con la contraseña de PostgreSQL

# 5. Crear la base de datos en PostgreSQL
psql -U postgres -c "CREATE DATABASE clinica;"

# 6. Aplicar migraciones
python manage.py migrate

# 7. Crear superusuario para el panel de administración
python manage.py createsuperuser

# 8. Iniciar el servidor de desarrollo
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Archivo `.env`

```env
DB_PASSWORD=tu_contraseña_postgres
```

## Rutas principales

| Ruta          | Descripción                    |
| ------------- | ------------------------------ |
| `/login/`     | Inicio de sesión               |
| `/panel/`     | Panel de control principal     |
| `/pacientes/` | Listado de pacientes           |
| `/doctores/`  | Listado de doctores            |
| `/horas/`     | Listado de citas médicas       |
| `/admin/`     | Panel de administración Django |

## Tests

Los tests validan el comportamiento de los modelos usando una base de datos de prueba temporal. Para ejecutarlos:

```bash
python manage.py test core.test
```

Cubren creación de registros, validaciones de campos y restricciones de unicidad (constraints) para los modelos `Paciente`, `Doctor` y `CitaMedica`.

## Estructura del proyecto

```
evaluacion_6/
├── clinica/              # Configuración del proyecto (settings, urls)
├── core/                 # Aplicación principal
│   ├── models.py         # Modelos: Paciente, Doctor, CitaMedica
│   ├── views.py          # Vistas basadas en clases (CBVs)
│   ├── forms.py          # Formularios con estilos Bootstrap
│   ├── urls.py           # Rutas de la aplicación
│   ├── admin.py          # Configuración del panel admin
│   ├── templates/        # Plantillas HTML
│   └── test/             # Tests unitarios por modelo
├── .env.example          # Plantilla de variables de entorno
├── requirements.txt      # Dependencias Python
└── manage.py
```
