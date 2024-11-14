from django.shortcuts import redirect, render

from app.models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})

def devs(request):
        if request.user.is_authenticated:
            return render (request, 'desenvolvedores.html')
        
        return redirect('/admin/login/?next=/')