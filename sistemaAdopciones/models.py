from django.db import models
from django.contrib.auth.models import AbstractUser



class Animal(models.Model):
       nombre = models.CharField(max_length=100)
       edad =  models.PositiveBigIntegerField()
       especie = models.CharField(max_length=50)
       raza = models.CharField(max_length=50, blank=True, null=True)
       descripcion = models.TextField()
       imagen = models.ImageField(upload_to='imagenes/animales')
       disponible = models.BooleanField(default=True)
       def __str__(self):
        return self.nombre
       
       
       
class SolicitudAdopcion(models.Model):
       usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
       animal = models.ForeignKey('Animal', on_delete= models.CASCADE)
       fecha_solicitud = models.DateTimeField(auto_now_add=True)
       estado = models.CharField(
              max_length= 20,
              choices= [
                     ('PENDIENTE', 'Pendiente'),
                     ('APROBADA', 'Aprobada'),
                     ('RECHAZADA', 'Rechazada'),
              ],
              default= 'PENDIENTE'
       )
       def __str__(self):
        return f"{self.usuario.username} - {self.animal.nombre}"
       
class Usuario(AbstractUser):
       telefono = models.CharField(max_length=15, blank=True, null=True)
       email = models.EmailField()
       direccion = models.CharField(max_length= 25, blank=True,null=True)
       TIPO_USUARIO_CHOICES = [
        ('ADOPTANTE', 'Adoptante'),
        ('ADMIN', 'Administrador'),
       ]
       tipo_usuario = models.CharField(max_length=14, choices=TIPO_USUARIO_CHOICES, default='ADOPTANTE')
       def __str__(self):
              return f"{self.tipo_usuario} - {self.email}"