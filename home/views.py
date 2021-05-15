from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def package(request):
    return render(request, 'package.html')
    #return HttpResponse("this is packages page")

def team(request):
    return render(request, 'team.html')
    #return HttpResponse("this is team page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        contact = Contact(email=email, name=name, city=city, state=state, phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, 'Message is sent.')
    return render(request, 'contact.html')
    #return HttpResponse("this is about page")

def student(request):
    return render(request, 'student.html')

def family(request):
    return render(request, 'family.html')

def senior(request):
    return render(request, 'senior.html')