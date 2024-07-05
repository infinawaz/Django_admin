from django.shortcuts import render
from django.http import HttpResponse
from . models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all
    return render(request, 'index.html', {'features': features}) 

def counter(request):
    text = request.POST['text']
    amtOfWords = len(text.split())
    return render(request, 'counter.html',{'amount': amtOfWords}) 