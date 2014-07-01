from django.db import models
from django.db.models import permalink


class InternalUrl(models.Model):
    slug = models.SlugField(max_length=10, unique=True)
    external_url = models.URLField(unique=True, max_length=255, blank=False)
    visited = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visited', '-created_at']

    def visit(self):
        self.visited += 1
        return self.save()
