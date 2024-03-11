from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class Ano(models.Model):
    ano = models.IntegerField(primary_key=True,choices=((i, i) for i in range(2009, 2024)))
    
    def __str__(self):
        return f'{self.ano}'
    

class Area(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)


    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
        
        
    def __str__(self) -> str:
        return self.nome
    
    
class Questao(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='areas')
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, related_name='questoes')
    contexto = models.CharField(max_length=300, null=False, blank=False)
    pergunta = models.CharField(max_length=300, null=False, blank=False)
    letra_a = models.CharField(max_length=300, null=False, blank=False)
    letra_b = models.CharField(max_length=300, null=False, blank=False)
    letra_c = models.CharField(max_length=300, null=False, blank=False)
    letra_d = models.CharField(max_length=300, null=False, blank=False)
    letra_e = models.CharField(max_length=300, null=False, blank=False)
    answer = models.CharField(max_length=1, null=False, blank=False)
    imagens = models.ImageField(upload_to='img_questoes', null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        
    
    def __str__(self) -> str:
        return f'{self.ano}-{self.area}-{self.id}'