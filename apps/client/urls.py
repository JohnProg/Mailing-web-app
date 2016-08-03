from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^dashboard/$', admin_view, name='dashboard'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
]
