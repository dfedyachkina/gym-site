from django.contrib import admin
from .models import Contact, GymContacts


class GymContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number']

    def has_add_permission(self, request):
        return not GymContacts.objects.exists()

    def has_change_permission(self, request, obj=None):
        return True


admin.site.register(Contact)
admin.site.register(GymContacts, GymContactAdmin)
