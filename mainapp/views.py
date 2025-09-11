# myapp/views.py
from django.shortcuts import render, redirect
from .models import Dbs

def index(request):
    return render(request, "index2.html")

def snd_hr(request):
    if request.method == 'POST':
        # Debug prints (only during development)
        print("POST keys:", request.POST.keys())
        print("FILES keys:", request.FILES.keys())

        name = request.POST.get('field1', '').strip()
        img = request.FILES.get('imgINP')   # this will be an UploadedFile when enctype is set

        # Optional: simple validation
        if not name:
            return render(request, 'index2.html', {'error': 'Name is required'})

        # Create and save model (Django will save the file to MEDIA_ROOT)
        obj = Dbs.objects.create(name=name, image=img)
        obj.save() #not necessary after create(), but harmless

        
    # GET -> render form
    return render(request, 'index.html')

def fk_db(request):
    return render(request, 'fk_db.html')


