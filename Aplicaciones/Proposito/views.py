from django.shortcuts import render

# Create your views here.

def propositos (request):
    return render(request, 'propositos.html')