from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

article = "wwwwwwwwwwwwwwwwwwwwwwww"

def index(request):
    return render(request, 'index.html', {'article': article})
    
