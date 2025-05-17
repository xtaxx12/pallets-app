from django.db import models

class Pallet(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    fecha = models.DateField()
    tipo = models.CharField(default='INGRESO', max_length=20)
    estado = models.CharField(choices=[('POR_RECIBIR', 'Por Recibir'), ('RECIBIDO', 'Recibido')], max_length=20)
    origen = models.CharField(max_length=100)
    desde_empresa = models.CharField(max_length=100)
    hacia_empresa = models.CharField(max_length=100)

