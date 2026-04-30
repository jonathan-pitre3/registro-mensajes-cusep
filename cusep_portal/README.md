# CUSEP Portal

## Español
Portal web para el Centro Universitario de Servicios y Estudios Psicológicos (CUSEP) de la Universidad de Puerto Rico, Recinto de Río Piedras.

## English
Web portal for the University Center for Psychological Services and Studies (CUSEP) at the University of Puerto Rico, Río Piedras Campus.

## Configuración / Setup
1. Clonar repositorio.
2. Crear y activar entorno virtual.
3. Instalar dependencias: `pip install -r requirements.txt`
4. Copiar variables: `cp .env.example .env`
5. Aplicar migraciones: `python manage.py migrate`
6. Ejecutar servidor: `python manage.py runserver`

## Datos de prueba
Ejecute `python manage.py seed_test_data` para crear 10 registros ficticios de solicitudes.

## Seguridad
Este sistema maneja información sensible. Antes de desplegar en producción debe completarse una revisión de seguridad y cumplimiento con HIPAA y la Ley 408 de Puerto Rico.

## GitHub policy
Nunca suba datos reales de pacientes, archivos `.env`, ni archivos de base de datos al repositorio.
