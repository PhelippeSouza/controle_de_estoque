from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model=Produto
        fields=['Código', 'Descrição','Tamanho' ,'Quantidade', 'Preço_unitário', 'Total' , 'Fornecedor']