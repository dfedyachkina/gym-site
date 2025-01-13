from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memberships")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Approved' if self.approved else 'Pending'}"


class Appointment(models.Model):
    TIME_CHOICES = [
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
    ]

    TRAINER_GENDER_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Doesn't Matter", "Doesn't Matter"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField(null=False, blank=False)
    time = models.CharField(max_length=5, choices=TIME_CHOICES, null=False, blank=False)
    trainer_gender = models.CharField(max_length=15, choices=TRAINER_GENDER_CHOICES, default="Doesn't Matter")
    is_member = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.user.username} on {self.date} at {self.time}"