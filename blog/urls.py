from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.admin_view, name='admin_view'),
]