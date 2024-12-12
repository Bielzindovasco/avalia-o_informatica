from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('marcas/', MarcaListView.as_view(), name='marca-list'),
    path('marcas/novo/', MarcaCreateView.as_view(), name='marca-create'),
    path('marcas/<int:pk>/editar/', MarcaUpdateView.as_view(), name='marca-update'),
    path('marcas/<int:pk>/deletar/', MarcaDeleteView.as_view(), name='marca-delete'),
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/novo/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/deletar/', CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('automoveis/', AutomovelListView.as_view(), name='automovel-list'),
    path('automoveis/novo/', AutomovelCreateView.as_view(), name='automovel-create'),
    path('automoveis/<int:pk>/editar/', AutomovelUpdateView.as_view(), name='automovel-update'),
    path('automoveis/<int:pk>/deletar/', AutomovelDeleteView.as_view(), name='automovel-delete'),
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/novo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/deletar/', ClienteDeleteView.as_view(), name='cliente-delete'),
]
