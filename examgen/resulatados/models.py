# resultados/models.py
from django.db import models
from django.contrib.auth.models import User
from examenes.models import Examen, Pregunta, Opcion

class RespuestaAlumno(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_texto = models.TextField(blank=True, null=True) # Solo para preguntas abiertas
    respuesta_opcion = models.ForeignKey(Opcion, blank=True, null=True, on_delete=models.SET_NULL) # Para opción múltiple
    respuesta_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.alumno.username} - {self.pregunta.texto}'

# resultados/models.py
class Calificacion(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=2) # Ej. 10.0
    fecha_calificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.alumno.username} - {self.puntuacion}'