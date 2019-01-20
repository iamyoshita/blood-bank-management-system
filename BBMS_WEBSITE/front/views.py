from django.shortcuts import render

# Create your views here.
"""from django.http import HttpResponse
from django.template import loader
def index(Response):
    template=loader.get_template('')
    return HttpResponse("<h1>---------------BLOOD BANK MANAGEMENT SYSTEM------------</h1><a href='http://127.0.0.1:8000/basic/admin/login/?next=/basic/admin/'>Admin Login</a>")"""
from django.shortcuts import render

# Create your views here
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import cover
def index(request):
    a=cover.objects.all()
    context={
        'a':a,
    }
    return render(request,'front/index.html',context)
