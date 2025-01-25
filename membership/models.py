from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('basic', 'Basic Membership'),
        ('premium', 'Premium Membership'),
        ('elite', 'Elite Membership'),
    ]
    name = models.CharField(max_length=50, choices=MEMBERSHIP_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='membership_images/', blank=True, null=True)  # noqa

    def __str__(self):
        return self.name


class Benefit(models.Model):
    membership = models.ForeignKey(Membership, related_name='benefits', on_delete=models.CASCADE)  # noqa
    description = models.TextField()

    def __str__(self):
        return self.description


class MembershipRequest(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)  # noqa

    def __str__(self):
        return f"{self.user.username} - {self.membership.name} ({self.get_status_display()})"  # noqa
