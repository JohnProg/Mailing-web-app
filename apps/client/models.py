# coding=utf-8
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(
        User
    )

    def __unicode__(self):
        return self.user.username
