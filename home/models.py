from datetime import datetime, timedelta

from django.db import models


class Advertising(models.Model):
    title = models.CharField(max_length=250, default='Aksiya')
    descriptions = models.TextField(null=True, blank=True)
    image = models.ImageField()
    # food_id = models.IntegerField(default=0)
    # new_price = models.IntegerField(default=0)
    start = models.DateTimeField(default=datetime.now())
    finish_date = models.DateTimeField(default=datetime.now() + timedelta(days=7),
                                       help_text='2000-12-31')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.descriptions[:30]

    class Meta:
        ordering = ['start']
