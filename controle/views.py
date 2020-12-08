from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required


@login_required

def lista_Produto(request):
    produto=Produto.objects.all()
    return render (request, 'produto.html', {'produto':produto})


def criar_Produto(request):

    form=ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'produto-form.html', {'form':form})


def update_Produto(request, id):
    produto=Produto.objects.get(id=id)
    form=ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produto')
    return render(request, 'produto-form.html', {'form':form, 'produto':produto})


def deletar_Produto(request, id):
    produto=Produto.objects.get(id=id)
    form=ProdutoForm(request.POST or None, instance=produto)
    if request.method=='POST':
        produto.delete()
        return redirect('lista_produto')
    return render(request, 'deletar_produto.html', {'produto':produto})                