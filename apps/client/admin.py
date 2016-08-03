from django.contrib import admin
from apps.client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Client, ClientAdmin)