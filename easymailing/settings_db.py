# coding=utf-8
"""
Django settings for project's DB.
"""
import os


def get_db():
    database = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('RDS_DB_NAME', 'easymailing'),
            'USER': os.environ.get('RDS_USERNAME', 'postgres'),
            'PASSWORD': os.environ.get('RDS_PASSWORD', 'admin'),
            'HOST': os.environ.get('RDS_HOSTNAME', 'localhost'),
            'PORT': os.environ.get('RDS_PORT', '5433'),
        }
    }
    return database
