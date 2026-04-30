from django.db import models


class SolicitudServicio(models.Model):
    # --- Tipo de Servicio ---
    TIPO_SERVICIO_CHOICES = [
        ('psicoterapia', 'Psicoterapia'),
        ('evaluacion', 'Evaluación Psicológica'),
    ]

    # --- Subtipo: Psicoterapia ---
    SUBTIPO_PSICOTERAPIA_CHOICES = [
        ('adulto', 'Adulto'),
        ('menor', 'Menor'),
        ('familia_pareja', 'Familia / Pareja'),
    ]

    # --- Subtipo: Evaluación ---
    SUBTIPO_EVALUACION_CHOICES = [
        ('adulto', 'Adulto'),
        ('menor', 'Menor'),
    ]

    # --- Tipo de Evaluación ---
    TIPO_EVALUACION_CHOICES = [
        ('psicologica_psicoeducativa_psicometrica', 'Evaluación psicológica / psicoeducativa / psicométrica'),
        ('neurodesarrollo', 'Evaluación del neurodesarrollo (ej. autismo)'),
        ('neuropsicologica', 'Evaluación neuropsicológica'),
    ]

    # --- Relación con el solicitante ---
    RELACION_CHOICES = [
        ('misma_persona', 'Misma persona'),
        ('madre_padre', 'Madre / Padre'),
        ('abuelo_abuela', 'Abuelo / Abuela'),
        ('encargado_cuidador', 'Encargado / Cuidador'),
        ('esposo_esposa', 'Esposo / Esposa'),
        ('persona_bajo_cuidado', 'Persona bajo mi cuidado / custodia'),
    ]

    # --- Status of the request (managed by staff) ---
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('contactado', 'Contactado'),
        ('completado', 'Completado'),
        ('archivado', 'Archivado'),
    ]

    # Stores the selected top-level service track.
    tipo_servicio = models.CharField(max_length=20, choices=TIPO_SERVICIO_CHOICES)
    # Stores psychotherapy audience subtype when psychotherapy is selected.
    subtipo_psicoterapia = models.CharField(max_length=30, choices=SUBTIPO_PSICOTERAPIA_CHOICES, blank=True, null=True)
    # Stores evaluation audience subtype when evaluation is selected.
    subtipo_evaluacion = models.CharField(max_length=10, choices=SUBTIPO_EVALUACION_CHOICES, blank=True, null=True)
    # Stores requested evaluation category for evaluation requests.
    tipo_evaluacion = models.CharField(max_length=60, choices=TIPO_EVALUACION_CHOICES, blank=True, null=True)

    # Full name of the person who will receive services.
    nombre_receptor = models.CharField(max_length=200, verbose_name='Nombre de persona que recibirá los servicios')
    # Age of the person receiving the requested service.
    edad_receptor = models.PositiveSmallIntegerField(verbose_name='Edad de la persona que recibirá los servicios')

    # Primary phone number for follow-up.
    telefono = models.CharField(max_length=20, verbose_name='Número de teléfono')
    # Primary email for follow-up.
    correo_electronico = models.EmailField(verbose_name='Correo electrónico')

    # Relationship between applicant and service recipient.
    relacion_con_receptor = models.CharField(max_length=30, choices=RELACION_CHOICES)
    # Applicant name when requesting on behalf of another person.
    nombre_solicitante = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nombre de quien solicita (si no es la misma persona)')

    # Internal workflow status managed by staff only.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    # Timestamp of when request was submitted.
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    # Internal notes for staff triage and tracking.
    notas_internas = models.TextField(blank=True, null=True, verbose_name='Notas internas del personal')

    class Meta:
        verbose_name = 'Solicitud de Servicio'
        verbose_name_plural = 'Solicitudes de Servicio'
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f"{self.nombre_receptor} — {self.get_tipo_servicio_display()} ({self.fecha_solicitud.strftime('%Y-%m-%d')})"
