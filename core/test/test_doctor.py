from django.test import TestCase
from core.models import Doctor
from datetime import date
class DoctorModelTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            nombre="Carlos",
            apellido="Méndez",
            especialidad="Cardiología",
            fecha_nacimiento=date(1995, 1, 1)
        )

    def test_info_doctor(self):
        """Validación 1: Verifica la representación _str_ Nombre y Apellido"""
        self.assertEqual(str(self.doctor), "Dr. Carlos Méndez - Cardiología")

    def test_especialidad_asignada(self):
        """Validación 2: Verifica que la especialidad se guarda correctamente"""
        self.assertEqual(self.doctor.especialidad, "Cardiología")

    def test_limite_caracteres_apellido(self):
        """Validación 3: Verifica que el apellido respete el max_length de 100"""
        field_label = self.doctor._meta.get_field('apellido').max_length
        self.assertEqual(field_label, 100)