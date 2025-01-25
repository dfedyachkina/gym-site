from django.shortcuts import render


def custom_404(request):
    return render(request, 'page404/404.html', status=404)
