from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models




class Tracker(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def days_left(self):
        if self.end_date:
            end_date = self.end_date.date()  # convert DateTime to date
            today = datetime.now().date()    # get current date
            return (end_date - today).days
        return None

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date must be after start date")
