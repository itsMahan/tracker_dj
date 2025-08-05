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
        if self.total_events:
            return self.total_events - self.used_events
        else:
            return None

    def increament_event(self):
        if not self.total_events:
            self.used_events += 1
            self.save()
        elif self.used_events < self.total_events:
            self.used_events += 1
            self.save()


    def decreament_event(self):
        if self.used_events > 0:
            self.used_events -= 1
            self.save()

