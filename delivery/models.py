from django.conf import settings
from django.db import models


class DeliveryTask(models.Model):
    LOW = "L"
    MEDIUM = "M"
    HIGH = "H"
    PRIORITIES = (
        (LOW, ("Low")),
        (MEDIUM, ("Medium")),
        (HIGH, ("High")),
    )
    title = models.CharField(max_length=150)
    creation = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    priority = models.CharField(choices=PRIORITIES, default=LOW, max_length=8)
