from membership.models import MembershipRequest


def membership_status(request):
    is_member = False
    if request.user.is_authenticated:
        is_member = MembershipRequest.objects.filter(
            user=request.user,
            status="approved"
        ).exists()
    return {"is_member": is_member}
