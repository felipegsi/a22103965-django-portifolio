from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Tarefa)

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)

admin.site.register(Conta)
admin.site.register(Area)
admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(Comentario)
