from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    empresa = models.CharField(max_length=300)
    log_date = models.DateTimeField("fecha del mensaje")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.empresa}' solicitado: {date.strftime('%A, %d %B, %Y at %X')}"
    
class LogEval(models.Model):
    #Ingesar variables requeridas en la base de datos para calcular resultado
    #Evaluar area de seguridad para despliegue de resultados (Verificar que no se pueda modificar<generar pdf>)
    
    def __str__(self) -> str:
        return super().__str__()
    
class Sector(models.Model):
    SECTOR_TIPO = {
        "PUBLICO": "Público",
        "PRIVADO": "Privado",
        "SOCIAL":"Social"
    }
    id_sector = models.Index
    sector = models.CharField(max_length=7, choices=SECTOR_TIPO)

class Sector_productivo(models.Model):
    tamaño = models.CharField(max_length=7)
    sector_productivo = models.CharField(max_length=21, unique=True)
    cant_personal = models.CharField(max_length=8, unique=True)
    
class Giro(models.Model):
    giro = models.CharField(max_length=9)
    actividad = models.CharField(max_length=15)

class Empresa(models.Model):
    nombre_ct = models.CharField(max_length=300)
    razon_social = models.CharField(max_length=20)
    rfc = models.CharField(max_length=50)
    equipo_seguridad = models.BooleanField
    equipo_seguridad_descripcion = models.TextField(max_length=300)
    adicional_logistica = models.TextField(max_length=200)
    multisitio = models.BooleanField(default=False)
    id_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    id_sector_productivo = models.ForeignKey(Sector_productivo, on_delete=models.CASCADE)
    id_giro = models.ForeignKey(Giro, on_delete=models.CASCADE)
    
