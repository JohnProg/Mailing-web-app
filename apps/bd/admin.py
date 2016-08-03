from django.contrib import admin
from apps.bd.models import ModuleContactListDB, Contact


class ModuleContactListDBAdmin(admin.ModelAdmin):
    list_display = ('owner', 'list_name', 'origin', 'destination', 'status', 'created_add', 'updated_add')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_and_last_name', 'email', 'list_owner',)

admin.site.register(ModuleContactListDB, ModuleContactListDBAdmin)
admin.site.register(Contact, ContactAdmin)