from django.contrib import admin

from .models import Disorder


@admin.register(Disorder)
class DisorderAdmin(admin.ModelAdmin):
    list_display = ['name']
