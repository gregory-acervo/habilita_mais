from django.contrib import admin
from .models import Cliente, AulaPratica, AulaTeorica, ExamePratico, ExameTeorico

#Register your models here

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone', 'email', 'data_criacao']
    search_fields = ['nome', 'cpf', 'email']

@admin.register(AulaTeorica)
class AulaTeoricaAdmin(admin.ModelAdmin):
    list_display = ['tema', 'presenca']

@admin.register(AulaPratica)
class AulaPraticaAdmin(admin.ModelAdmin):
    list_display = ['percurso', 'presenca']

@admin.register(ExameTeorico)
class ExameTeoricoAdmin(admin.ModelAdmin):
    list_display = ['nota', 'resultado']

@admin.register(ExamePratico)
class ExamePraticoAdmin(admin.ModelAdmin):
    list_display = ['faltas', 'resultado']
