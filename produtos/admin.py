from django.contrib import admin
from .models import Produto, Posicao, Usuario


admin.site.register(Produto)
admin.site.register(Posicao)
admin.site.register(Usuario)

# Register your models here.
