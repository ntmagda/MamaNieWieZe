from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404

from django.views import generic
from .models import Entry
from django.utils import timezone
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/index.html"
    paginate_by = 4

class AboutUs(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/aboutus.html"
    paginate_by = 4

class ExpeditionsView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/expeditions.html"
    paginate_by = 4

class VideoView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/video.html"
    paginate_by = 2

# class PostView(generic.ListView):
#     queryset = models.Entry.objects.published()
#     template_name = "blog/post.html"
#     paginate_by = 4

class ContactView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/contact.html"
    paginate_by = 2


def readmore(request, entry_slug):
    entry = get_object_or_404(Entry, slug=entry_slug)
    return render(request, 'blog/article.html', {
            'entry': entry,
            'error_message': "You didn't select a choice.",
        })


class PostView(generic.DetailView):
    template_name = 'blog/post.html'
    model = Entry

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        return context

