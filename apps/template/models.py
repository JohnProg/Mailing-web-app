# coding=utf-8
from django.utils.translation import ugettext as _
from django.db import models
from apps.client.models import Client
from apps.extra.constants import PUBLISH_CHOICES, STATUS_UNPUBLISHED, SELECTED_CHOICES, STATUS_NO_SELECTED, \
    TEMPLATE_TYPE_CHOICES, TYPE_MAILING


class Template(models.Model):
    """
    Template model for the super administrator
    """
    template_name = models.CharField(
        max_length=60
    )
    content = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='media/template/'
    )
    image_url = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    status = models.IntegerField(
        choices=PUBLISH_CHOICES,
        default=STATUS_UNPUBLISHED
    )
    created_add = models.DateTimeField(
        editable=False,
        auto_now_add=True
    )
    updated_add = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    def __unicode__(self):
        return self.template_name

    class Meta:
        verbose_name = 'Plantilla'
        verbose_name_plural = 'Plantillas'

    @property
    def as_dict(self):
        template = {
            'id': self.id,
            'template_name': self.template_name,
            'image_url': self.image_url,
            'status': self.status,
            'content': self.content,
            'created_add': self.created_add.strftime('%d/%m/%Y') if self.created_add else '',
            'updated_add': self.updated_add.strftime('%d/%m/%Y') if self.updated_add else ''
        }
        return template


class ModuleTemplate(models.Model):
    """
    Template module model
    """
    owner = models.ForeignKey(
        Client,
        verbose_name='Cliente',
        help_text='Seleccionar al cliente o usuario'
    )
    template_name = models.CharField(
        max_length=60,
        verbose_name=_("Template name")
    )
    colors = models.TextField(
        null=True,
        blank=True
    )
    status = models.IntegerField(
        choices=PUBLISH_CHOICES,
        default=STATUS_UNPUBLISHED
    )
    cover_image = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    module_template = models.ForeignKey(
        Template,
        null=True,
        blank=True
    )
    base64_url = models.TextField(
        null=True,
        blank=True
    )
    selected = models.IntegerField(
        choices=SELECTED_CHOICES,
        default=STATUS_NO_SELECTED
    )

    def __unicode__(self):
        return self.template_name

    class Meta:
        verbose_name = 'Modulo Plantilla'
        verbose_name_plural = 'Modulo Plantillas'

    @property
    def as_dict(self):
        module_template = {
            'id': self.id,
            'template_name': self.template_name,
            'status': self.status,
            'cover_image': self.cover_image,
            'colors': self.colors,
            'selected': self.selected

        }
        return module_template