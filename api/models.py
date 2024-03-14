from django.db import models

class Cedente(models.Model):
    razao_social = models.CharField(max_length=150, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False)
    
    def __str__(self):
        return self.razao_social
    
class Banco(models.Model):
    BANCOS = (
        ('001', 'Banco do Brasil'),
        ('033', 'Santander'),
        ('104', 'Caixa'),
        ('237', 'Bradesco'),
        ('341', 'Itaú'),
    )
    CNAB = (
        ('1', '240'),
        ('2', '400'),
    )

    nome = models.CharField(max_length=150, blank=False, null=False, choices=BANCOS)
    cnab = models.CharField(max_length=1, blank=False, null=False, choices=CNAB)
    
    def __str__(self):
        return self.nome
    