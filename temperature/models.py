from django.conf import settings
from django.db import models
from django.utils import timezone

class Temp(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    temperture = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        sttemp = str(self.temperture)
        return sttemp