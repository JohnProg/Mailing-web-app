from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^create/$',
        create_or_modify_mailing_campaign),
    url(r'^get/(?P<mailing_id>\d+)/$',
        get_mailing_campaign),
    url(r'^update/(?P<mailing_id>\d+)/$',
        create_or_modify_mailing_campaign),
    url(r'^list/$', mailing_list),
    url(r'^delete/(?P<mailing_id>\d+)/$', delete_mailing),
    # Statistics
    url(r'^(?P<mailing_id>\d+)/statistics/$',
        get_data_from_tag_for_statistics),
    url(r'^(?P<mailing_id>\d+)/statistics-detail/$',
        get_data_info_from_tag_for_statistics),
]
