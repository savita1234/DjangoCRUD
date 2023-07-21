from django.shortcuts import render, HttpResponse
from vege.models import *

# Create your views here.
def index(request):
    receipes = Receipe.objects.all()
    context = {'receipes': receipes}
    return render(request, 'main.html',context)
    #return HttpResponse("hello is homepage")

def index2(request, id):
    receipe = Receipe.objects.get(id = id)
    context = {'receipe' : receipe }
    return render(request, 'main_2.html',context)
