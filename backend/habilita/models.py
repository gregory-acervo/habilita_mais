from django.db import models

# Create your models here.

# Arrumar as ForeignKeys e ver se coloca slug ou id

class Cliente(models.Model):
    nome = models.CharField(max_length=300)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome


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

    class Meta:
        verbose_name = "Aula Teórica"
        verbose_name_plural = "Aulas Teóricas"

class AulaPratica(EtapaFormacao):
    #instrutor = models.ForeignKey(...)
    #veiculo = models.ForeignKey(...)
    percurso = models.CharField(max_length=400)
    presenca = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Aula Prática"
        verbose_name_plural = "Aulas Práticas"

class ExameTeorico(EtapaFormacao):
    #aplicador = models.ForeignKey(...)
    nota = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True
    )
    resultado = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Exame Teórico"
        verbose_name_plural = "Exames Teóricos"

class ExamePratico(EtapaFormacao):
    #examinador = models.ForeignKey(...)
    #veiculo = models.ForeignKey(...)
    faltas = models.PositiveIntegerField(default=0)
    resultado = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Exame Prático"
        verbose_name_plural = "Exames Práticos"