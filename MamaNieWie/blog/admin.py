from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin
from . import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from models import Article_Image
from adminfiles.admin import FilePickerAdmin

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> ' %\
                (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class ImageInLine(admin.TabularInline):
    model = Article_Image
    extra = 1


class EntryAdmin(FilePickerAdmin):
    list_display = ("title", "created", "modified", "admin_thumbnail")
    fields = ("title", "body", "title_image", "slug")
    readonly_fields = ("admin_thumbnail",)

    inlines = [ImageInLine]
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'title_image':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(EntryAdmin,self).formfield_for_dbfield(db_field, **kwargs)
admin.site.register(models.Entry, EntryAdmin)

