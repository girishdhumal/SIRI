from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
   return render(request, 'index.html')
   # return HttpResponse("GIRISH")

def about(request):
   return HttpResponse("About")

def services(request):
   return HttpResponse("About")

def contact(request):
   return render(request, 'contact.html')






    