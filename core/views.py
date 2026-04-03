from django.urls import reverse_lazy
from .models import Paciente, Doctor, CitaMedica
from .forms import PacienteForm, DoctorForm, CitaMedicaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# --- PANEL PRINCIPAL ---

class PanelControlView(LoginRequiredMixin, TemplateView):
    template_name ='core/panel_control.html'


# --- GESTIÓN DE PACIENTES ---

class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name='core/pacientes/listar.html'
    context_object_name='pacientes'

    def get_queryset(self):
        # Filtro ORM: capturamos el parámetro 'q' de la URL
        query = self.request.GET.get('q')
        if query:
            # Filtramos pacientes cuyo nombre contenga el texto buscado
            return Paciente.objects.filter(nombre__icontains=query)
        return Paciente.objects.all()


class PacienteCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('listar_paciente')
    success_message = 'Paciente creado con éxito.'


class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'core/pacientes/eliminar.html'
    success_url = reverse_lazy('listar_paciente')

    def form_valid(self, form):
        messages.success(self.request, 'Paciente eliminado con éxito')
        return super().form_valid(form)

class PacienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('listar_paciente')
    success_message = 'Paciente actualizado con éxito.'

# --- GESTIÓN DE DOCTORES (Lógica idéntica a Pacientes) ---

class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'core/doctores/listar.html'
    context_object_name = 'doctores'

class DoctorCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctores/form.html'
    success_url = reverse_lazy('listar_doctor')
    success_message = 'Doctor creado con éxito.'

class DoctorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctores/form.html'
    success_url = reverse_lazy('listar_doctor')
    success_message = 'Doctor actualizado con éxito.'


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'core/doctores/eliminar.html'
    success_url = reverse_lazy('listar_doctor')

    def form_valid(self, form):
        messages.success(self.request, 'Doctor eliminado con éxito.')
        return super().form_valid(form)

class CitaListView(LoginRequiredMixin, ListView):
    model = CitaMedica
    template_name = 'core/horas/listar.html'
    context_object_name = 'horas'

    def get_queryset(self):
        queryset = super().get_queryset()
        fecha = self.request.GET.get('fecha')
        paciente = self.request.GET.get('paciente')

        if fecha:
            queryset = queryset.filter(fecha=fecha)
        if paciente:
            queryset = queryset.filter(paciente__nombre__icontains=paciente)
        
        return queryset

class CitaCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = CitaMedica
    template_name = 'core/horas/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('listar_hora')
    success_message = 'Cita Médica creada con éxito.'

class CitaUpdateView (LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CitaMedica
    template_name = 'core/horas/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('listar_hora')
    success_message = 'Cita Médica actualizada con éxito.'

class CitaDeleteView(LoginRequiredMixin, DeleteView):
    model = CitaMedica
    template_name = 'core/horas/eliminar.html'
    success_url = reverse_lazy('listar_hora')

    def form_valid(self, form):
        messages.success(self.request, 'Cita Médica eliminada con éxito.')
        return super().form_valid(form)
    
