from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Set the creation time only if the contact is being created for the first time
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)
