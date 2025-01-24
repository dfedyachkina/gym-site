from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'page 404/404.html', status=404)