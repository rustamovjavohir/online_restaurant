from django.db import models


class Advertising(models.Model):
    descriptions = models.TextField(null=True, blank=True)
    image = models.ImageField()
    start = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.descriptions[:30]

    class Meta:
        ordering = ['start']
