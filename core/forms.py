from django import forms
from .models import Paciente, Doctor, CitaMedica

# --- FORMULARIOS (VALIDACIÓN Y HTML) ---
# Django Forms convierte modelos de BD en formularios HTML listos para usar en templates.
# Se encarga también de VALIDAR los datos que vienen del usuario.

class PacienteForm(forms.ModelForm):
    """
    Formulario automático basado en el modelo Paciente.
    """
    class Meta:
        model = Paciente      # Modelo base
        fields = '__all__'    # Incluir todos los campos definidos en el modelo
        
        # 'widgets' nos permite personalizar cómo se renderiza el input HTML
        # Aquí agregamos clases CSS de Bootstrap ('form-control') para el diseño.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            # Usamos type="date" nativo de HTML5 para el selector de fecha
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class DoctorForm(forms.ModelForm):
    """
    Formulario para CRUD de registro de Doctores.
    """
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CitaMedicaForm(forms.ModelForm):
    """
    Formulario para gestionar las Horas Médicas.
    Las claves foráneas (ForeignKey) se renderizan automáticamente como SELECTS (<select>).
    """
    class Meta:
        model = CitaMedica
        fields = '__all__'
        widgets = {
            # 'form-select' es la clase especial de Bootstrap 5 para dropdowns
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), # Caja de texto multilínea
        }
