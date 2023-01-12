from django.shortcuts import render
from .models import *


def home(request):
    return render(request,'home.html')

def blog(request):
    data = {
        'maqolalar': Maqola.objects.all().order_by('-sana')
    }
    return render(request,'blog.html',data)
def meeting(request):
    data = {
        'dates':Intervyu.objects.all().order_by('-sana')
    }
    return render(request,'intervyu.html',data)

def maqola(request,son):
    data = {
        'm':Maqola.objects.get(id=son)

    }
    return render(request,'maqola.html',data)

def intervyu(request,num):
    data = {
        'i':Intervyu.objects.get(id=num)
    }
    return render(request,'meeting.html',data)
def about(request):
    return render(request,'about.html')




# Create your views here.
