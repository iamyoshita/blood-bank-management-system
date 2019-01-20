from django.shortcuts import render

# Create your views here
from django.template import loader
from django.http import HttpResponse,Http404
from .models import Donor,Receiver,Bank,Staff
def all_donors(request):
    all_records=Donor.objects.all()
    return render(request, "Blood_bank/group.html", {'all_records':all_records})
def all_receivers(request):
    all_r=Receiver.objects.all()
    return render(request,"Blood_bank/receive.html",{'all_r':all_r})
