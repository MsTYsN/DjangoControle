from django.contrib import admin

# Register your models here.
from .models import Client, Compte, Operation


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
    pass

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass