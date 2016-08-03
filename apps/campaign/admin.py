from django.contrib import admin
from apps.campaign.models import ModuleCampaign


class ModuleCampaignAdmin(admin.ModelAdmin):
    list_display = (
        'campaign_name', 'from_name', 'reply_email', 'template_campaign', 'owner', 'date_create', 'date_send',)
    list_filter = ('status',)
    search_fields = ['campaign_name', 'from_name', 'reply_email', 'template_campaign__template_name']


admin.site.register(ModuleCampaign, ModuleCampaignAdmin)
