from django.db import models

# Modelo para Persona
class Persona(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('PA', 'Pasaporte'),
        ('CE', 'Cédula de Extranjería'),
    ]

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    numero_celular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# Modelo para Vacuna
class Vacuna(models.Model):
    TIPOS_VACUNAS = [
        ('COVID-19', 'Vacuna contra el COVID-19'),
        ('Influenza', 'Vacuna contra la Influenza'),
        ('Tétanos', 'Vacuna contra el Tétanos'),
    ]

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='vacunas')
    tipo_vacuna = models.CharField(max_length=20, choices=TIPOS_VACUNAS)
    fecha_aplicacion = models.DateField()

    def __str__(self):
        return f"{self.tipo_vacuna} - {self.persona.nombre}"
