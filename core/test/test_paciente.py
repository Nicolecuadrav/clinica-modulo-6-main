from django.test import TestCase
from datetime import date, timedelta
from core.models import Paciente

class PacienteModelTest(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nombre="Agustina",
            apellido="Rossi",
            fecha_nacimiento=date(1990, 1, 1)
        )

    def test_nombre_completo(self):
        """Validación 1: Verifica la representación __str__ Nombre y Apellido"""
        self.assertEqual(str(self.paciente), "Agustina Rossi")
        
    def test_edad_calculada_dinamica(self):
        """Validación 2: Verifica el cálculo de edad con la fecha actual """
        hoy = date.today()
        esperado = hoy.year - 1990
        if (hoy.month, hoy.day) < (1, 1):
            esperado -= 1
        self.assertEqual(self.paciente.edad, esperado)

    def test_limite_caracteres_apellido(self):
        """Validación 3: Verifica que el apellido respete el max_length de 100 """
        field_label = self.paciente._meta.get_field('apellido').max_length
        self.assertEqual(field_label, 100)