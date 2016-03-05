from __future__ import unicode_literals

from django.db import models

from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from django.conf import settings


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)



class Entry(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title_image = models.ImageField(upload_to=settings.MEDIA_URL, null=True)

    objects = EntryQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def get_image_filename(instance, filename):
        title =instance.entry.title
        return "media/%s" % filename


    def admin_thumbnail(self):
        return u'<img src="%s" />' % self.title_image.url
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

class Article_Image(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to=settings.MEDIA_URL, null=True)
