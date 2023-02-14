from django.shortcuts import render
from testApp.models import HydJobs,PuneJobs,BalJobs,MumJobs
# Create your views here.
def home(request):
    return render(request,'testApp/home.html')

def hydJobs(request):
    hydjob=HydJobs.objects.order_by('date')
    n='Hydrabad'
    data={
        'jobs':hydjob,
        'n':n,
        'i1':'h1.jpg',
        'i2':'h2.jpg',
        'i3':'h3.jpg'
    }
    return render(request,'testApp/jobs.html',context=data)


def puneJobs(request):
    puneJob=PuneJobs.objects.order_by('date')
    n='Pune'
    data={
        'jobs':puneJob,
        'n':n,
        'i1':'p1.jpg',
        'i2':'p2.jpg',
        'i3':'p3.jpg'
    }
    return render(request,'testApp/jobs.html',context=data)

def balJobs(request):
    BalJob=BalJobs.objects.order_by('date')
    n='Bangalore'
    data={
        'jobs':BalJob,
        'n':n,
        'i1':'sorry.png',
    }
    return render(request,'testApp/jobs.html',context=data)

def mumJobs(request):
    MumJob=MumJobs.objects.order_by('date')
    n='Mumbai'
    data={
        'jobs':MumJob,
        'n':n,
        'i1':'sorry.png',
    }
    return render(request,'testApp/jobs.html',context=data)
