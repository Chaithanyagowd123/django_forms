from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def create_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}                      #empty topic form object

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is creted')
        
        else:
            return HttpResponse('invalid data')
    

    return render(request,'create_topic.html',d)



def create_webpage(request):
    EWTO=WebpageForm()
    d={'EWTO':EWTO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            nm=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ur)[0]
            WO.save()

            return HttpResponse('webpage object is create')
        else:
            return HttpResponse('invalid data')
        
    return render(request,'create_webpage.html',d)

def create_accessrecords(request):
    EAWO=AccessRecordsForm()
    d={'EAWO':EAWO}
    if request.method=='POST':
        EAFO=AccessRecordsForm(request.POST)
        if EAFO.is_valid():
            nm=EAFO.cleaned_data['name']
            dt=EAFO.cleaned_data['date']
            atr=EAFO.cleaned_data['author']
            WO=Webpage.objects.get(pk=nm)
            AO=AccessRecords.objects.get_or_create(name=WO,date=dt,author=atr)[0]
            AO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Data is invalid')

    return render(request,'create_accessrecords.html',d)




