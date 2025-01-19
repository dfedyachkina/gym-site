from django.db import models


class GymContacts(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Gym Contact Information"


