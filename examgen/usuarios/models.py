# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ES_PROFESOR = 'profesor'
    ES_ALUMNO = 'alumno'

    ROL_CHOICES = [
        (ES_PROFESOR, 'Profesor'),
        (ES_ALUMNO, 'Alumno'),
    ]

    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default=ES_ALUMNO)

    # Añadir related_name para evitar el conflicto
    groups = models.ManyToManyField(
        "auth.Group",
        related_name='usuarios_groups',  # Cambiar el related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name="usuario",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_user_permissions', # Cambiar el related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name="usuario",
    )

    def __str__(self):
        return self.username