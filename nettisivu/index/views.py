from django.shortcuts import render, HttpResponse
from .models import Distro

def index(req):
    return render(req, "index/index.html")

def distro(req):
    distrot = Distro.objects.all()
    return render(req, "index/distrot.html", {'distrot': distrot})

def toinensivu(req):

    return render(req, "index/toinensivu.html")