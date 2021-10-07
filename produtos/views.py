from django.shortcuts import redirect, render
from .models import Produto
from .forms import ProdutoForm

def lista_produtos (request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos}) 
    #Com a lista de produtos criada funçao render que vai retornar a request e criar um .html pra criar a lista de protudos


def criar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produtosform.html', {'form' : form})

    # Vai verificar se o form do produto é valido, caso nao seja, ele vai retornar em branco pro usuario registrar um novo produto

def update_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance= produto)

    if form.is_valid():
        form.save()
        return redirect ('lista_produtos')

    return render(request, 'produtosform.html', {'form': form, 'produto' : produto})

    #Verifica que o form é valido/preenchido podendo redirecionar para lista de produtos inicial e pelo id vai atualizar o produto

def deleta_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect (lista_produtos)
    #verifica se o request é POST, pois, quando a pessoa clicar em delete o request é GET, entao ja entra direto na tela de confirmacao do delete
    return render (request, 'deletaprodutoconfirm.html', {'produto' : produto})
    #tela de confirmacao pro deletar, seguranca
