from datetime import datetime
from markdown import markdown
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from docs.utils import slugify


class HackerearthDoc(MPTTModel):
    """
    A model for storing hackerearth documentations
    """
    user = models.ForeignKey(User, verbose_name=_("Author"), db_index=True)
    timestamp = models.DateTimeField(blank=True, db_index=True)
    title = models.CharField(_("Title"), max_length=255, default='')
    slug = models.CharField(max_length=255, db_index=True, blank=True)
    published = models.BooleanField(default=False, db_index=True)
    is_document = models.BooleanField(default=False, db_index=True)
    body = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    full_slug = models.CharField(_("URL"), max_length=255, blank=True,
            db_index=True, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
            related_name='children')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.now()
        if self.body:
            self.body_html = markdown(self.body, safe_mode=False)
        if not self.slug:
            self.slug = slugify(self.title)

        orig_full_slug = self.full_slug

        if self.parent:
            self.full_slug = "/".join([self.parent.full_slug, self.slug])
        else:
            self.full_slug = self.slug

        super(HackerearthDoc, self).save(*args, **kwargs)

        # This is where if we moves an entire node which contains many more
        # nodes full_slug for each i.e children node, children's children node
        # gets updated
        if orig_full_slug != self.full_slug:
            for child in self.get_children():
                child.save()
