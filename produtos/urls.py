from django.urls import path
from .views import lista_produtos, criar_produto, update_produto, deleta_produto

urlpatterns = [
    path('', lista_produtos, name= 'lista_produtos'),
    path('new', criar_produto, name = 'criar_produto'),
    path('update/<int:id>/', update_produto, name= 'update_produto'),
    path('delete/<int:id>/', deleta_produto, name= 'deleta_produto'),
]
