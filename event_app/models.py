from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    total_events = models.PositiveIntegerField(null=True, blank=True)
    used_events = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def remaining_events(self):
        return self.total_events - self.used_events

    def increament_event(self):
        if self.used_events < self.total_events:
            self.used_events += 1
            self.save()

    def decrement_event(self):
        self.used_events -= 1
        self.save()