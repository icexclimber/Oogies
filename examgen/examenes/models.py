# examenes/models.py
from django.db import models
from django.contrib.auth.models import User

class Examen(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    profesor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# examenes/models.py
class Pregunta(models.Model):
    examen = models.ForeignKey(Examen, related_name="preguntas", on_delete=models.CASCADE)
    texto = models.TextField()
    tipo = models.CharField(max_length=50, choices=[('multiple', 'Opción múltiple'), ('abierta', 'Respuesta abierta')])

    def __str__(self):
        return self.texto

# examenes/models.py
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)  # Corregido a 200 para coincidir con Examen
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto