from django.contrib import admin
from .models import Tarefa
from .models import Airport
from .models import Flight
from .models import Passenger

# Register your models here.
admin.site.register(Tarefa)

admin.site.register(Airport)

admin.site.register(Flight)

admin.site.register(Passenger)
