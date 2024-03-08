from django.shortcuts import render
from .models import Questao

# Create your views here.

def index(request):
    questoes = Questao.objects.all()
    
    context = {
        'questoes': questoes
    }
    
    return render(request, 'questao/index.html', context)