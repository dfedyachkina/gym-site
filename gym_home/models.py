from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# Model for Carousel Image
class Carousel(models.Model):
    image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=255, blank=True, null=True) 
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title if self.title else f"Carousel Image {self.id}"


# Model for Home Text Content
class HomeText(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
