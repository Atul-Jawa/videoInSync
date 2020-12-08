from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'page': 'index', 'include': 'index.html'})

def watchtogether(request):
    return render(request, 'watchtogether.html', {'page':'contactus'})