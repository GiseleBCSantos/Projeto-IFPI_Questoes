from import_export.forms import ImportForm, ConfirmImportForm, forms
from .models import Area, Ano

class CustomImportForm(ImportForm):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), required=True)
    ano = forms.ModelChoiceField(queryset=Ano.objects.all(), required=True)

class CustomConfirmImportForm(ConfirmImportForm):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), required=True)
    ano = forms.ModelChoiceField(queryset=Ano.objects.all(), required=True)
    
