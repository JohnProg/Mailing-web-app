# coding=utf-8
from django.db import models
from apps.bd.models import ModuleContactListDB
from apps.client.models import Client
from apps.extra.constants import PUBLISH_CHOICES, STATUS_UNPUBLISHED
from apps.template.models import ModuleTemplate


class ModuleCampaign(models.Model):
    """
    Campaign module model
    """
    owner = models.ForeignKey(
        Client,
        verbose_name='Cliente',
        help_text='Seleccionar al cliente o usuario'
    )
    template_campaign = models.ForeignKey(
        ModuleTemplate,
        verbose_name='Plantilla'
    )
    list_contacts = models.ManyToManyField(
        ModuleContactListDB,
        verbose_name='Lista de Contactos'
    )
    campaign_name = models.CharField(
        max_length=60,
        verbose_name='Nombre'
    )
    from_name = models.CharField(
        max_length=120,
        verbose_name='From'
    )
    reply_email = models.EmailField(
        verbose_name='Reply',
        null=True,
        blank=True
    )
    subject = models.CharField(
        verbose_name='Asunto',
        max_length=120,
        null=True,
        blank=True
    )
    link_redirect_to = models.URLField(
        verbose_name='Redirigir hacia',
        max_length=200,
        null=True,
        blank=True
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
    )
    date_send = models.DateTimeField(
        verbose_name='Fecha de envío',
        null=True,
        blank=True
    )
    status = models.IntegerField(
        choices=PUBLISH_CHOICES,
        default=STATUS_UNPUBLISHED,
        verbose_name='Estado'
    )
    title = models.CharField(
        verbose_name='Texto del título de la plantilla',
        max_length=60,
        null=True,
        blank=True
    )
    subtitle = models.CharField(
        verbose_name='Texto del subtítulo de la plantilla',
        max_length=60,
        null=True,
        blank=True
    )
    body_section1 = models.TextField(
        verbose_name='Texto del párrafo 1 de la plantilla',
        null=True,
        blank=True
    )
    body_section2 = models.TextField(
        verbose_name='Texto del párrafo 2 de la plantilla',
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.campaign_name

    class Meta:
        verbose_name = 'Modulo Campana'
        verbose_name_plural = 'Modulo Campanas'

    @property
    def as_dict(self):
        mailing = {
            'id': self.id,
            'campaign_name': self.campaign_name,
            'from_name': self.from_name,
            'reply_email': self.reply_email,
            'subject': self.subject,
            'link_redirect_to': self.link_redirect_to,
            'date_create': self.date_create.strftime('%d/%m/%Y') if self.date_create else '',
            'date_send': self.date_send.strftime('%d/%m/%Y') if self.date_send else '',
            'status': self.status,
        }
        return mailing

    @property
    def as_dict2(self):
        list_contacts = self.list_contacts.values('id')
        list_contacts = [contact.get('id') for contact in list_contacts]
        mailing = {
            'id': self.id,
            'campaign_name': self.campaign_name,
            'from_name': self.from_name,
            'reply_email': self.reply_email,
            'subject': self.subject,
            'link_redirect_to': self.link_redirect_to,
            'template_id': self.template_campaign_id,
            'date_create': self.date_create.strftime('%d/%m/%Y %H:%M:%S') if self.date_create else '',
            'date_send': self.date_send.strftime('%d/%m/%Y %H:%M:%S') if self.date_send else '',
            'status': self.status,
            'title': self.title,
            'subtitle': self.subtitle,
            'body_section1': self.body_section1,
            'body_section2': self.body_section2,
            'list_contacts': list_contacts
        }
        return mailing


class MandrillSent(models.Model):
    """
    Mandrill Sent data
    """
    status = models.CharField(max_length=20)
    _id = models.CharField(max_length=36)
    email = models.EmailField()
    reject_reason = models.CharField(max_length=20, null=True)
