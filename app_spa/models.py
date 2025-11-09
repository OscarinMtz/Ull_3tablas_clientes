from django.db import models

class Clientes(models.Model):
    id_clientes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    alergias = models.TextField(blank=True, null=True)
    preferencias = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"