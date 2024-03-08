from django.contrib import admin
from .models import Area, Questao
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(Questao)
class QuestaoAdmin(ImportExportModelAdmin):
    list_display = ['ano', 'area']
    search_fields = ['ano', 'area']