import re
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import SolicitudServicio


class SolicitudServicioForm(forms.ModelForm):
    class Meta:
        model = SolicitudServicio
        exclude = ['status', 'fecha_solicitud', 'notas_internas']
        labels = {
            'tipo_servicio': 'Tipo de servicio',
            'subtipo_psicoterapia': 'Subtipo de psicoterapia',
            'subtipo_evaluacion': 'Subtipo de evaluación',
            'tipo_evaluacion': 'Tipo de evaluación',
            'nombre_receptor': 'Nombre de la persona que recibirá los servicios',
            'edad_receptor': 'Edad de la persona que recibirá los servicios',
            'telefono': 'Número de teléfono',
            'correo_electronico': 'Correo electrónico',
            'relacion_con_receptor': 'Relación con la persona que recibirá los servicios',
            'nombre_solicitante': 'Si no es usted quien recibirá los servicios, indique su nombre completo',
        }
        help_texts = {
            'tipo_servicio': 'Seleccione el servicio principal que desea solicitar.',
            'subtipo_psicoterapia': 'Seleccione la población para psicoterapia.',
            'subtipo_evaluacion': 'Seleccione la población para evaluación.',
            'tipo_evaluacion': 'Seleccione el tipo de evaluación que necesita.',
            'nombre_receptor': 'Escriba nombre y apellido.',
            'edad_receptor': 'Edad entre 1 y 120 años.',
            'telefono': 'Formato sugerido: 787-000-0000',
            'correo_electronico': 'Usaremos este correo para contactarle.',
            'relacion_con_receptor': 'Indique su relación con la persona que recibirá el servicio.',
            'nombre_solicitante': 'Campo requerido cuando solicita por otra persona.',
        }
        widgets = {
            'tipo_servicio': forms.RadioSelect,
            'subtipo_psicoterapia': forms.RadioSelect,
            'subtipo_evaluacion': forms.RadioSelect,
            'tipo_evaluacion': forms.RadioSelect,
            'relacion_con_receptor': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(*[Field(name) for name in self.fields])
        self.fields['edad_receptor'].widget.attrs.update({'min': 1, 'max': 120})
        self.fields['telefono'].widget.attrs.update({'pattern': r'^\d{3}-?\d{3}-?\d{4}$', 'placeholder': '787-000-0000'})

    def clean(self):
        cleaned_data = super().clean()
        tipo_servicio = cleaned_data.get('tipo_servicio')
        relacion = cleaned_data.get('relacion_con_receptor')
        edad = cleaned_data.get('edad_receptor')
        telefono = cleaned_data.get('telefono')

        if tipo_servicio == 'psicoterapia' and not cleaned_data.get('subtipo_psicoterapia'):
            self.add_error('subtipo_psicoterapia', 'Debe seleccionar un subtipo de psicoterapia.')

        if tipo_servicio == 'evaluacion':
            if not cleaned_data.get('subtipo_evaluacion'):
                self.add_error('subtipo_evaluacion', 'Debe seleccionar un subtipo de evaluación.')
            if not cleaned_data.get('tipo_evaluacion'):
                self.add_error('tipo_evaluacion', 'Debe seleccionar un tipo de evaluación.')

        if relacion != 'misma_persona' and not cleaned_data.get('nombre_solicitante'):
            self.add_error('nombre_solicitante', 'Este campo es obligatorio cuando solicita por otra persona.')

        if edad is not None and (edad < 1 or edad > 120):
            self.add_error('edad_receptor', 'La edad debe estar entre 1 y 120 años.')

        if telefono and not re.match(r'^\d{3}-?\d{3}-?\d{4}$', telefono):
            self.add_error('telefono', 'El número debe tener 10 dígitos y puede incluir guiones (ej. 787-000-0000).')

        return cleaned_data
