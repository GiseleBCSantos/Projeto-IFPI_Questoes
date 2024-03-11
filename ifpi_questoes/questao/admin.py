from django.contrib import admin
from .models import Area, Questao, Ano
from import_export.admin import ImportExportModelAdmin, ImportMixin
# from import_export import ImportMixin
from .forms import CustomImportForm, CustomConfirmImportForm
from .resources import QuestaoResource

# Register your models here.

admin.site.register(Ano)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']



class CustomQuestaoAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['ano', 'area']
    filter_display = [['ano', 'area']]
    resource_classes = [QuestaoResource]
    import_form_class = CustomImportForm
    confirm_form_class = CustomConfirmImportForm
    
    def get_confirm_form_initial(self, request, import_form):
        initial = super().get_confirm_form_initial(request, import_form)
        if import_form:
            initial['nome'] = import_form.cleaned_data['area']
            initial['ano'] = import_form.cleaned_data['ano']
        return initial
    
admin.site.register(Questao, CustomQuestaoAdmin)