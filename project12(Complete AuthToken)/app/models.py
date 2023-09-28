from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ExpiringToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    expiration = models.DateTimeField(default=timezone.now)  # Add an expiration date

    def is_expired(self):
        return self.expiration < timezone.now()