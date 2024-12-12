from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Marca, Categoria, Automovel, Cliente


def home(request):
    return render(request, 'home.html')


class MarcaListView(ListView):
    model = Marca
    template_name = 'marca/list.html'

class MarcaCreateView(CreateView):
    model = Marca
    fields = ['nome', 'pais_origem']
    template_name = 'marca/form.html'
    success_url = reverse_lazy('marca-list')

class MarcaUpdateView(UpdateView):
    model = Marca
    fields = ['nome', 'pais_origem']
    template_name = 'marca/form.html'
    success_url = reverse_lazy('marca-list')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marca/confirm_delete.html'
    success_url = reverse_lazy('marca-list')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'categoria/form.html'
    success_url = reverse_lazy('categoria-list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'categoria/form.html'
    success_url = reverse_lazy('categoria-list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/confirm_delete.html'
    success_url = reverse_lazy('categoria-list')


class AutomovelListView(ListView):
    model = Automovel
    template_name = 'automovel/list.html'

class AutomovelCreateView(CreateView):
    model = Automovel
    fields = ['modelo', 'preco', 'marca', 'categoria']
    template_name = 'automovel/form.html'
    success_url = reverse_lazy('automovel-list')

class AutomovelUpdateView(UpdateView):
    model = Automovel
    fields = ['modelo', 'preco', 'marca', 'categoria']
    template_name = 'automovel/form.html'
    success_url = reverse_lazy('automovel-list')

class AutomovelDeleteView(DeleteView):
    model = Automovel
    template_name = 'automovel/confirm_delete.html'
    success_url = reverse_lazy('automovel-list')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'email']
    template_name = 'cliente/form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'email']
    template_name = 'cliente/form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/confirm_delete.html'
    success_url = reverse_lazy('cliente-list')
