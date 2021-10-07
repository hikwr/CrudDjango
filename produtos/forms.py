from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'quantidade', 'posicao']
        labels = {
            'descricao' : 'Descrição',
            'preco' : 'Preço',
            'quantidade' : 'Quantidade',
            'posicao' : 'Posição,'
        }