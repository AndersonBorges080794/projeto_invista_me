from django.db import models
from datetime import datetime
'''
Serão as colunas da tabela:
* investimento
* valor
* pago
* data
'''
#Modelo que representa o banco de dados
class Investimento(models.Model):
    Investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    
    

