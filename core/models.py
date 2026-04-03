from django.db import models
from datetime import date
# --- DEFINICIÓN DE MODELOS (TABLAS DE BASE DE DATOS) ---
# Cada clase aquí representa una tabla en la base de datos (PostgreSQL/SQLite).
# Los atributos de la clase son las columnas de esa tabla.

class Paciente(models.Model):
    """
    Modelo que representa a un paciente en el sistema.
    Tabla resultante en BD: core_paciente
    """
    nombre = models.CharField(max_length=100)           # Texto corto (VARCHAR)
    apellido = models.CharField(max_length=100)         # Texto corto (VARCHAR) 
    fecha_nacimiento = models.DateField()               # Solo fecha (sin hora)

    @property #Este decorador, ahce que no se guarde edad en la DB, sino que se calcule en el momento, asi no guardas fecha de nacimiento y edad que seria redundante
    def edad(self):
        fecha_actual = date.today()
        # Calculamos la diferencia de años
        edad = fecha_actual.year - self.fecha_nacimiento.year
        #Valor booleano para saber si aun no ha pasado su fecha de cumpleaños este año
        cumplio_años = (fecha_actual.month, fecha_actual.day) >= (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        #Operador ternario, dice si ya cumplio años retorna edad, si aun no retorna edad -1
        return edad if cumplio_años else edad - 1
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['apellido']

    def __str__(self):
        """Representación en texto del objeto (se ve así en el admin)."""
        return f"{self.nombre} {self.apellido}"

class Doctor(models.Model):
    """
    Modelo que representa a un médico o especialista.
    Tabla resultante en BD: core_doctor
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length=100)

    @property #Este decorador, ahce que no se guarde edad en la DB, sino que se calcule en el momento, asi no guardas fecha de nacimiento y edad que seria redundante
    def edad(self):
        fecha_actual = date.today()
        # Calculamos la diferencia de años
        edad = fecha_actual.year - self.fecha_nacimiento.year
        #Valor booleano para saber si aun no ha pasado su fecha de cumpleaños este año
        cumplio_años = (fecha_actual.month, fecha_actual.day) >= (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        #Operador ternario, dice si ya cumplio años retorna edad, si aun no retorna edad -1
        return edad if cumplio_años else edad - 1

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ['apellido']

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"

class CitaMedica(models.Model):
    """
    Modelo que representa una hora médica reservada.
    Actúa como tabla intermedia que vincula Pacientes con Doctores.
    Tabla resultante en BD: core_citamedica
    """
    # ForeignKey: Crea una relación Relacional (Uno a Muchos). 
    # on_delete=models.CASCADE: Si borras al Paciente/Doctor, se borran sus citas automáticamente.
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    fecha = models.DateField()   # Día de la cita
    hora = models.TimeField()    # Hora exacta de la cita
    motivo = models.TextField()  # Texto largo para describir la razón de la consulta
    class Meta:
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"
        ordering = ['-fecha', '-hora'] # El '-' indica orden descendente
        constraints = [
        # Evita que un DOCTOR tenga dos citas a la misma hora/fecha
        models.UniqueConstraint(
            fields=['doctor', 'fecha', 'hora'], 
            name='cita_unica_doctor'
        ),
        # Evita que un PACIENTE tenga dos citas a la misma hora/fecha
        models.UniqueConstraint(
            fields=['paciente', 'fecha', 'hora'], 
            name='cita_unica_paciente'
        ),
    ]

    def __str__(self):
        return f"Cita: {self.paciente.nombre} con Dr. {self.doctor.apellido} - {self.fecha} {self.hora}"
