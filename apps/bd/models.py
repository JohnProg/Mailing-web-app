# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.client.models import Client
from apps.extra.constants import FIELD_TO_CHOOSE, PUBLISH_CHOICES, STATUS_UNPUBLISHED


class ModuleContactListDB(models.Model):
    """
    ContactList module model
    """
    owner = models.ForeignKey(
        Client
    )
    list_name = models.CharField(
        max_length=120,
        verbose_name=_(u'Title')
    )
    origin = models.IntegerField(
        choices=FIELD_TO_CHOOSE,
        null=False
    )
    destination = models.IntegerField(
        choices=FIELD_TO_CHOOSE,
        null=False
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
        auto_now=True
    )

    def __str__(self):
        return self.list_name

    @property
    def as_dict(self):
        bad_contacts_quantity = Contact.objects.filter(list_owner=self, status=0).count()
        good_contacts_quantity = Contact.objects.filter(list_owner=self, status=1).count()
        module_db = {
            'id': self.id,
            'list_name': self.list_name,
            'owner': self.owner.user.email,
            'origin': self.origin,
            'destination': self.destination,
            'status': self.status,
            'good_contacts': good_contacts_quantity,
            'bad_contacts': bad_contacts_quantity,
            'created_add': self.created_add.strftime('%d/%m/%Y') if self.created_add else '',
            'updated_add': self.updated_add.strftime('%d/%m/%Y') if self.updated_add else '',
        }
        return module_db

    @property
    def as_dict2(self):
        bad_contacts = Contact.objects.filter(list_owner=self, status=0)
        bad_contacts = [contact.as_dict for contact in bad_contacts]

        good_contacts = Contact.objects.filter(list_owner=self, status=1)
        good_contacts = [contact.as_dict for contact in good_contacts]

        module_db = {
            'id': self.id,
            'list_name': self.list_name,
            'owner': self.owner.user.email,
            'origin': self.origin,
            'destination': self.destination,
            'status': self.status,
            'good_contacts': good_contacts,
            'bad_contacts': bad_contacts,
            'created_add': self.created_add.strftime('%d/%m/%Y') if self.created_add else '',
            'updated_add': self.updated_add.strftime('%d/%m/%Y') if self.updated_add else '',
        }
        return module_db


class Contact(models.Model):
    """
    Contact model
    """
    name_and_last_name = models.CharField(
        max_length=120
    )
    email = models.EmailField(
        max_length=40
    )
    list_owner = models.ForeignKey(
        ModuleContactListDB
    )
    status = models.IntegerField(
        choices=PUBLISH_CHOICES,
        default=STATUS_UNPUBLISHED,
        verbose_name='Estado'
    )

    def __unicode__(self):
        return self.name_and_last_name

    @property
    def as_dict(self):
        contact = {
            'id': self.id,
            'name': self.name_and_last_name,
            'email': self.email,
            'status': self.status
        }
        return contact
