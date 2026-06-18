from django.db import models

# Create your models here.

# Arrumar as ForeignKeys e ver se coloca slug ou id

class EtapaFormacao(models.Model):
    #aluno = models.ForeignKey(...)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    observacoes = models.TextField(blank=True)

    class Meta:
        abstract = True

class AulaTeorica(EtapaFormacao):
    #instrutor = models.ForeignKey(...)
    tema = models.CharField(max_length=200)
    presenca = models.BooleanField(default=False)


class AulaPratica(EtapaFormacao):
    #instrutor = models.ForeignKey(...)
    #veiculo = models.ForeignKey(...)
    percurso = models.CharField(max_length=400)
    presenca = models.BooleanField(default=False)

class ExameTeorico(EtapaFormacao):
    #aplicador = models.ForeignKey(...)
    nota = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True
    )
    resultado = models.CharField(max_length=20)

class ExamePratico(EtapaFormacao):
    #examinador = models.ForeignKey(...)
    #veiculo = models.ForeignKey(...)
    faltas = models.PositiveIntegerField(default=0)
    resultado = models.CharField(max_length=20)