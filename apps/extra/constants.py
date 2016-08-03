#! coding: utf-8
from django.utils.translation import ugettext as _


STATUS_UNPUBLISHED = 0
STATUS_PUBLISHED = 1

PUBLISH_CHOICES = (
    (STATUS_UNPUBLISHED, _('Unpublished')),
    (STATUS_PUBLISHED, _('Published'))
)

STATUS_NO_SELECTED = 0
STATUS_SELECTED = 1

SELECTED_CHOICES = (
    (STATUS_NO_SELECTED, _('Not Selected')),
    (STATUS_SELECTED, _('Selected'))
)

TYPE_MAILING = 0
TYPE_TEMPLATE = 1

TEMPLATE_TYPE_CHOICES = (
    (TYPE_MAILING, _('Mailing Template')),
    (TYPE_TEMPLATE, _('Module Template'))
)

NAME = 1
EMAIL = 2

FIELD_TO_CHOOSE = (
    (NAME, _('Name')),
    (EMAIL, _('Email'))
)