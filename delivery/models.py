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
    NEW = "NW"
    ACCEPTED = "AC"
    COMPLETED = "CM"
    DECLINED = "D"
    CANCELLED = "CN"
    STATES = (
        (NEW, ("New")),
        (ACCEPTED, ("Accepted")),
        (COMPLETED, ("Completed")),
        (DECLINED, ("Declined")),
        (CANCELLED, ("Cancelled")),
    )
    title = models.CharField(max_length=150)
    creation = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    priority = models.CharField(choices=PRIORITIES, default=LOW, max_length=8)
    states = models.CharField(choices=STATES, default=NEW, max_length=9)

    def __str__(self):
        return self.title
