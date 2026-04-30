from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='SolicitudServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(choices=[('psicoterapia', 'Psicoterapia'), ('evaluacion', 'Evaluación Psicológica')], max_length=20)),
                ('subtipo_psicoterapia', models.CharField(blank=True, choices=[('adulto', 'Adulto'), ('menor', 'Menor'), ('familia_pareja', 'Familia / Pareja')], max_length=30, null=True)),
                ('subtipo_evaluacion', models.CharField(blank=True, choices=[('adulto', 'Adulto'), ('menor', 'Menor')], max_length=10, null=True)),
                ('tipo_evaluacion', models.CharField(blank=True, choices=[('psicologica_psicoeducativa_psicometrica', 'Evaluación psicológica / psicoeducativa / psicométrica'), ('neurodesarrollo', 'Evaluación del neurodesarrollo (ej. autismo)'), ('neuropsicologica', 'Evaluación neuropsicológica')], max_length=60, null=True)),
                ('nombre_receptor', models.CharField(max_length=200, verbose_name='Nombre de persona que recibirá los servicios')),
                ('edad_receptor', models.PositiveSmallIntegerField(verbose_name='Edad de la persona que recibirá los servicios')),
                ('telefono', models.CharField(max_length=20, verbose_name='Número de teléfono')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('relacion_con_receptor', models.CharField(choices=[('misma_persona', 'Misma persona'), ('madre_padre', 'Madre / Padre'), ('abuelo_abuela', 'Abuelo / Abuela'), ('encargado_cuidador', 'Encargado / Cuidador'), ('esposo_esposa', 'Esposo / Esposa'), ('persona_bajo_cuidado', 'Persona bajo mi cuidado / custodia')], max_length=30)),
                ('nombre_solicitante', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de quien solicita (si no es la misma persona)')),
                ('status', models.CharField(choices=[('pendiente', 'Pendiente'), ('contactado', 'Contactado'), ('completado', 'Completado'), ('archivado', 'Archivado')], default='pendiente', max_length=20)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('notas_internas', models.TextField(blank=True, null=True, verbose_name='Notas internas del personal')),
            ],
            options={'verbose_name': 'Solicitud de Servicio', 'verbose_name_plural': 'Solicitudes de Servicio', 'ordering': ['-fecha_solicitud']},
        ),
    ]
