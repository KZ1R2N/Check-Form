# form/models.py
from django.db import models

class FormData(models.Model):
    # Input Fields
    number_field = models.IntegerField(null=True, blank=True)
    text_field = models.CharField(max_length=255, null=True, blank=True)
    date_field = models.DateField(null=True, blank=True)

    # Checkbox Flags (to check if the field should be included)
    is_number_checked = models.BooleanField(default=False)
    is_text_checked = models.BooleanField(default=False)
    is_date_checked = models.BooleanField(default=False)

    def __str__(self):
        return f"Form Data #{self.id}"
