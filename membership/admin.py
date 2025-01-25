from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Membership, Benefit, MembershipRequest


class MembershipAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name', 'description')


class BenefitAdmin(SummernoteModelAdmin):
    list_display = ('membership', 'description')
    search_fields = ('membership__name', 'description')


class MembershipRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership', 'request_date', 'status', 'approved_date')  # noqa
    list_filter = ('status', 'membership', 'request_date')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status=MembershipRequest.APPROVED)
    approve_requests.short_description = "Approve selected requests"

    def reject_requests(self, request, queryset):
        queryset.update(status=MembershipRequest.REJECTED)
    reject_requests.short_description = "Reject selected requests"

    def approved_date(self, obj):
        if obj.status == MembershipRequest.APPROVED:
            return obj.request_date
        return "-"
    approved_date.admin_order_field = 'request_date'


admin.site.register(Membership, MembershipAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(MembershipRequest, MembershipRequestAdmin)
