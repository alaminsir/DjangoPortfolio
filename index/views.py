from django.shortcuts import render
from .models import about as aboutmodel

# Create your views here.
def home(request):
    aboutdata = aboutmodel.objects.all()[0]
    context ={
        'about':aboutdata
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')