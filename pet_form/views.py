from urllib import request

from django.shortcuts import render, redirect, get_object_or_404  # type: ignore[import]
from .models import Pet

def home(request):
    if request.method == "POST":
        username=request.POST["username"]
        name=request.POST["name"]
        color=request.POST["color"]
        behavior = ", ".join(request.POST.getlist("behavior"))
        breed = request.POST["breed"]
        
        pets = Pet.objects.create(
            username=username,
            name=name,
            color=color,
            behavior=behavior,
            breed=breed,
)

        return redirect('home')
    
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})

def dashboard(request):

    pets = Pet.objects.all()

    action = None

    if request.method == "POST":

        action = request.POST.get("action")

    return render(request, 'dashboard.html', {
        'pets': pets,
        'action': action
    })
# Create your views here.
