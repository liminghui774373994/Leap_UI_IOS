from django.db import models

# Create your models here.

from django.db import models


class information(models.Model):
    event_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    content_type = models.CharField(unique=True, max_length=255, blank=True, null=True)
    teacher_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    search_type = models.CharField(unique=True, max_length=255, blank=True, null=True)
    content = models.CharField(unique=True, max_length=255, blank=True, null=True)
    query = models.CharField(unique=True, max_length=255, blank=True, null=True)
    location_id = models.CharField(unique=True, max_length=255, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'information'