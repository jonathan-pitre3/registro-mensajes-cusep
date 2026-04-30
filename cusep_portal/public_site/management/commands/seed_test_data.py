from django.core.management.base import BaseCommand
from public_site.models import SolicitudServicio


class Command(BaseCommand):
    help = 'Genera datos de prueba ficticios para SolicitudServicio.'

    def handle(self, *args, **options):
        self.stdout.write('ADVERTENCIA: Estos son datos de prueba ficticios. Nunca utilice datos reales en el ambiente de desarrollo.')
        status_values = ['pendiente', 'contactado', 'completado', 'archivado']
        for i in range(1, 11):
            tipo = 'psicoterapia' if i % 2 else 'evaluacion'
            SolicitudServicio.objects.create(
                tipo_servicio=tipo,
                subtipo_psicoterapia='adulto' if tipo == 'psicoterapia' else None,
                subtipo_evaluacion='menor' if tipo == 'evaluacion' else None,
                tipo_evaluacion='neuropsicologica' if tipo == 'evaluacion' else None,
                nombre_receptor=f'Persona Prueba {i}',
                edad_receptor=20 + i,
                telefono=f'787-000-00{i:02d}',
                correo_electronico=f'prueba{i}@test.com',
                relacion_con_receptor='misma_persona' if i % 3 else 'madre_padre',
                nombre_solicitante='Prueba Doe' if i % 3 == 0 else '',
                status=status_values[(i - 1) % 4],
            )
        self.stdout.write(self.style.SUCCESS('Datos de prueba creados exitosamente.'))
