from django.contrib import admin
from apps.template.models import Template, ModuleTemplate


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('template_name',)


class ModuleTemplateAdmin(admin.ModelAdmin):
    list_display = ('template_name',)

admin.site.register(Template, TemplateAdmin)
admin.site.register(ModuleTemplate, ModuleTemplateAdmin)