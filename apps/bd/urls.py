from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^create/$',
        create_or_modify_module_db),
    url(r'^get/(?P<module_db_id>\d+)/$',
        get_module_db),
    url(r'^update/(?P<module_db_id>\d+)/$',
        create_or_modify_module_db),
    url(r'^list/$', module_db_list),
    url(r'^delete/(?P<module_db_id>\d+)/$', delete_module_db),
    url(r'^delete-contacts/(?P<module_db_id>\d+)/$', delete_contacts_module_db),
    url(r'^import-csv/(?P<module_db_id>\d+)/$', import_file_to_mailing_db),
    url(r'^(?P<module_db_id>\d+)/add-contact/$', add_contact_data_to_contact_list),
]
