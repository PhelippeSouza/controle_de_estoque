from django.db import models

class Produto(models.Model):
    Código = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    Descrição = models.CharField(max_length=100)
    Quantidade = models.DecimalField(max_digits=4, decimal_places=0)
    Preço_unitário = models.DecimalField(max_digits=10, decimal_places=4,null=True)
    Total = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    Tamanho=models.CharField(max_length=4, null=True)
    Fornecedor=models.CharField(max_length=230, null=True)
 
    
    def _str_(self):
        return self.Descrição



