from django.db import models
class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('basic', 'Basic Membership'),
        ('premium', 'Premium Membership'),
        ('elite', 'Elite Membership'),
    ]
    
    name = models.CharField(max_length=50, choices=MEMBERSHIP_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='membership_images/', blank=True, null=True)

    def __str__(self):
        return self.name
