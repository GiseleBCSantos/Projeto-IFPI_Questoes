from import_export import resources
from .models import Questao

class QuestaoResource(resources.ModelResource):    
    class Meta:
        model = Questao
