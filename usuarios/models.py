# usuarios/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, identify_hasher

# Create your models here.


class Usuario(AbstractUser):
    ROLES_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('CAJERO', 'Cajero'),
    ]

    rol = models.CharField(
        max_length=6, choices=ROLES_CHOICES, default='CAJERO')
    pin_autorizacion = models.CharField(max_length=6, null=True, blank=True,
                                        help_text="Pin numerico de 6 digitos para autorizacion de transacciones")
    
    def save(self, *args, **kwargs):
        if self.pin_autorizacion and not self.pin_autorizacion.startswith('pbkdf2_sha256$'):
            self.pin_autorizacion = make_password(self.pin_autorizacion)
        super().save(*args, **kwargs)

    def verificar_pin(self, pin):
        if not self.pin_autorizacion:
            return False
        try:
            hasher = identify_hasher(self.pin_autorizacion)
            return hasher.verify(pin, self.pin_autorizacion)
        except ValueError:
            return False
    

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"
