from django.test import TestCase
from core.models import CitaMedica, Paciente, Doctor
from datetime import date, time
from django.db import IntegrityError

class CitaMedicaModelTest(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nombre='Martina',
            apellido='Martinolli',
            fecha_nacimiento=date(1990, 5, 15)
        )
        self.doctor = Doctor.objects.create(
            nombre='Carlos',
            apellido='Torres',
            fecha_nacimiento=date(1975, 3, 10),
            especialidad='Cardiología'
        )
    
    def test_creacion_cita(self):
        cita = CitaMedica.objects.create(
            paciente=self.paciente,
            doctor=self.doctor,
            fecha=date(2026, 4, 10),
            hora=time(10, 0),
            motivo='Checkeo anual'
        )
        # Verifica que se guardó en la BD
        self.assertEqual(CitaMedica.objects.count(), 1)
        # Verifica el formato de __str__
        #Nombre paciente
        self.assertIn('Martina', str(cita))
        #Apellido doctor
        self.assertIn('Torres', str(cita))
    
    def test_constraint_doctor_mismo_horario(self):
        #Este test busca validar la uniqueconstraint del modelo en CitaMedica.Meta
        CitaMedica.objects.create(
            paciente=self.paciente,
            doctor=self.doctor,
            fecha=date(2026, 4, 10),
            hora=time(10, 0),
            motivo='Primera cita, test mismo horario'
        )
        # Crear un segundo paciente para que la colisión sea por el doctor
        otro_paciente = Paciente.objects.create(
            nombre='Pedro',
            apellido='Mamani',
            fecha_nacimiento=date(1985, 8, 20)
        )
        with self.assertRaises(IntegrityError):
            CitaMedica.objects.create(
                paciente=otro_paciente,
                doctor=self.doctor,       # mismo doctor
                fecha=date(2026, 4, 10),  # misma fecha
                hora=time(10, 0),         # misma hora
                motivo='Segunda cita, mismo horario'
            )

    def test_constraint_paciente_mismo_horario(self):
        #Este test busca validar la uniqueconstraint del modelo en CitaMedica.Meta
        CitaMedica.objects.create(
            paciente=self.paciente,
            doctor=self.doctor,
            fecha=date(2026, 4, 10),
            hora=time(10, 0),
            motivo='Primera cita'
        )
        # Crear un segundo doctor para que la colisión sea por el paciente
        otro_doctor = Doctor.objects.create(
            nombre='María',
            apellido='Rojas',
            fecha_nacimiento=date(1980, 1, 5),
            especialidad='Pediatría'
        )
        with self.assertRaises(IntegrityError):
            CitaMedica.objects.create(
                paciente=self.paciente,   # mismo paciente
                doctor=otro_doctor,
                fecha=date(2026, 4, 10),  # misma fecha
                hora=time(10, 0),         # misma hora
                motivo='Segunda cita mismo paciente, diferente doctor'
            )