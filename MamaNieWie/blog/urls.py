__author__ = 'MagdaNT'
from django.conf.urls import url, patterns
from django.conf import settings
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^home/$', views.BlogIndex.as_view(), name='home'),
    url(r'^aboutus/$', views.AboutUs.as_view(), name='aboutus'),
    url(r'^expeditions/$', views.ExpeditionsView.as_view(), name='expeditions'),
    url(r'^gallery/$', views.VideoView.as_view(), name='video'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^article/(?P<entry_slug>[-\w]+)/$', views.readmore, name='readmore'),
    url(r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += patterns('',  url(r'^media/img/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.MEDIA_ROOT, }),)
