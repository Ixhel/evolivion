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
    
class Empresa(models.Model):
    SECTOR = {
        "PUBLICO": "Público",
        "PRIVADO": "Privado",
        "SOCIAL": "Social"
    }
    GIRO = {
        "COMERCIO": "Comercio",
        "INDUSTRIA": "Industria",
        "SERVICIOS": "Servicios"
    }
    TAMAÑO = {
        "MICRO": "Micro",
        "PEQUEÑA": "Pequeña",
        "MEDIANA": "Mediana",
        "GRANDE": "Grande"
    }
    id_empresa = models.BigAutoField(primary_key=True)
    nombre_ct = models.CharField(max_length=300)
    razon_social = models.CharField(max_length=20)
    rfc = models.CharField(max_length=128)
    equipo_seguridad = models.BooleanField(default=False)
    equipo_seguridad_descripcion = models.TextField(max_length=300)
    adicional_logistica = models.TextField(max_length=200)
    sector = models.CharField(max_length=8, choices=SECTOR)
    giro = models.CharField(max_length=10, choices=GIRO)
    tamaño = models.CharField(max_length=8, choices=TAMAÑO)
    multisitio = models.BooleanField(default=False)
    directivo = models.CharField(max_length=128)
    
class Domicilio_empresa(models.Model):
    id_domicilio = models.BigAutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="empresa relacionada[domicilio primario]")
    cp = models.PositiveIntegerField
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    no_ext = models.PositiveIntegerField
    no_int = models.PositiveIntegerField
    
class Multisitio(models.Model):
    id_multisitio = models.BigAutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="empresa relacionada[domicilio secundario]")
    cp = models.PositiveIntegerField
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    no_ext = models.PositiveIntegerField
    no_int = models.PositiveIntegerField
    
class Encargado_ct(models.Model):
    id_encargado = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=25)
    correo = models.EmailField
    telefono = models.AutoField
    extension = models.PositiveSmallIntegerField
    id_empresa = models.ManyToManyField(Empresa, through="Certificacion", verbose_name="empresa a cargo")

class Asesor_certificador(models.Model):
    id_asesor = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    registro = models.CharField(max_length=25)

class Certificacion(models.Model):
    TIPO = {
        "INICIAL": "Inicial",
        "VIGILANCIA": "Vigilancia",
        "RENOVACION": "Renovación"
    }
    id_certificacion = models.BigAutoField(primary_key=True, unique=True)
    fecha = models.DateField(auto_now=True)
    tipo = models.CharField(max_length=10, choices=TIPO)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="empresa certificada")
    
    id_asesor = models.ManyToManyField(Asesor_certificador, verbose_name="asesor para la certificacion")
    id_encargado_ct = models.ForeignKey(Encargado_ct, on_delete=models.SET_NULL, verbose_name="encargado del centro de trabajo certificado")
    
    personal_tiempo_completo = models.PositiveSmallIntegerField
    personal_medio_tiempo = models.PositiveSmallIntegerField
    alcance = models.PositiveSmallIntegerField
    motivos = models.TextField

class Documentos(models.Model):
    id_archivo = models.BigAutoField(primary_key=True, unique=True)
    id_certificacion = models.ForeignKey(Certificacion, on_delete=models.CASCADE, verbose_name="certificacion relacionada")
    politica_igualdad = models.FileField
    apendice_B = models.FileField
    codigo_etica = models.FileField