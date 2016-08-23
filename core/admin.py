from django.contrib import admin
from .models import Campo, Reserva, Cliente
# Register your models here.
admin.site.register(Campo)
admin.site.register(Reserva)
admin.site.register(Cliente)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
