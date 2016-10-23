from django.db import models
import uuid

class Show(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=4096)
    description = models.CharField(max_length=4096)
    location = models.CharField(max_length=1024)
    registration_deadline = models.DateTimeField()
    registration_link = models.CharField(max_length=1024)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
