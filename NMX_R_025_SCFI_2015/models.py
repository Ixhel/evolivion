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
    #
    def __str__(self) -> str:
        return super().__str__()
