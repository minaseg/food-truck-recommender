from django.db import models


class UserPreference(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    preference = models.CharField(max_length=255)

    def __str__(self):
        return f"Preferences at ({self.latitude}, {self.longitude})"
