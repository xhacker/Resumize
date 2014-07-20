from django.db import models


class Resume(models.Model):
    data = models.CharField(max_length=10240, blank=True)
