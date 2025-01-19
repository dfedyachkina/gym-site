from django.db import models


class GymContacts(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Gym Contact Information"


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    comment = models.TextField()

    def __str__(self):
        return f"Contact request from {self.first_name} {self.last_name}"

