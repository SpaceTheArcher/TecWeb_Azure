from django.db import models

# Create your models here.

class Curso(models.Model):
    
    carga_horaria = models.IntegerField("Carga Horária")
    nome = models.CharField("Nome",max_length = 20)
    tipo = models.CharField("Tipo",max_length = 20)
    professor = models.CharField("Professor",max_length=50)