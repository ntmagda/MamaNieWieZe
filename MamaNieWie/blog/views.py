from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/index.html"
    paginate_by = 2

class AboutUs(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/aboutus.html"
    paginate_by = 2

class ExpeditionsView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/expeditions.html"
    paginate_by = 2

class VideoView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/video.html"
    paginate_by = 2

class ContactView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/contact.html"
    paginate_by = 2
