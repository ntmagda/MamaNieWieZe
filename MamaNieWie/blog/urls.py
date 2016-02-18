__author__ = 'MagdaNT'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='index'),
]
