from django.contrib import admin
from .models import Personagem

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']