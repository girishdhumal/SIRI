from django.shortcuts import render, HttpResponse
from datetime import datetime
from SIRI.models import Contact
from SIRI.models import User
# Create your views here.
def index(request):
   return render(request, 'index.html')
   # return HttpResponse("GIRISH")

def about(request):
   #  if request.method =="POST":
   #    name = request.POST.get('name')
   #    # phone = request.POST.get('phone')
   #    email = request.POST.get('email')
   #    # password = request.POST.get('password')
   #    user = User(name=name, email=email)
   #    user.save()
    return render(request, 'about.html')
   

def services(request):
   return HttpResponse("#")

def contact(request):
   if request.method =="POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      desc = request.POST.get('desc')
      contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
      contact.save()
   return render(request, 'contact.html')






    