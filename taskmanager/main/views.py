from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .models import Complex
from .models import Massage
from .models import Apparat

def index(request):
    return render(request, 'main/index.html')

def complex(request):
    comp = Complex.objects.all()
    return render(request, 'main/complex.html', {'comp': comp})

def contact(request):
    return render(request, 'main/contact.html')

def apparat(request):
    appar = Apparat.objects.all()
    return render(request, 'main/hardware_correction.html', {'appar': appar})

def massaje(request):
    mass = Massage.objects.all()
    return render(request, 'main/massaje.html', {'mass': mass})

def sales(request):
    tasks = Task.objects.all()
    return render(request, 'main/sales.html', {'tasks': tasks})







