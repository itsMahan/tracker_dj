from datetime import datetime

from django.db import models

# Create your models here.


class Counter(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def days_passed(self):
        days = (datetime.now().date() - self.start_date.date()).days
        return days
