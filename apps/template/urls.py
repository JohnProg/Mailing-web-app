from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^create/$',
        create_or_modify_module_template),
    url(r'^get/(?P<module_template_id>\d+)/$',
        get_module_template),
    url(r'^update/(?P<module_template_id>\d+)/$',
        create_or_modify_module_template),
    url(r'^list/$', module_template_list),
    url(r'^general-list/$', template_list),
    url(r'^delete/(?P<module_template_id>\d+)/$', delete_module_template),
]
