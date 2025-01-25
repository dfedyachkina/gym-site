from django.shortcuts import render, get_object_or_404, reverse
from .models import Carousel, HomeText


def home(request):
    carousel_images = Carousel.objects.filter(is_active=True)
    home_text = HomeText.objects.filter(is_active=True).first()

    return render(request, 'gym_home/home.html', {'carousel_images': carousel_images, 'home_text': home_text})  # noqa
