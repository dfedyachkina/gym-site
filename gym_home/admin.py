from django.contrib import admin
from .models import Carousel, HomeText
from django_summernote.admin import SummernoteModelAdmin

# Carousel Model Admin
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    ordering = ('order',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else "No Image"
    
    image_preview.short_description = 'Image Preview'

# HomeText Model Admin
class HomeTextAdmin(SummernoteModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'content')

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(HomeText, HomeTextAdmin)