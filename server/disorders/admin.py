from django.contrib import admin

from .models import Disorders


@admin.register(Disorders)
class DisorderAdmin(admin.ModelAdmin):
    list_display = ['name']
