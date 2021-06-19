from django.shortcuts import render, HttpResponse
my={"hi":"hu",}

def index(request):
  return render(request,'test.html',my)

def about(request):
  return HttpResponse("hello world this is about page")

def services(request):
  return HttpResponse("hello world this is servicespage")

def contact(request):
  return render(request,"Contact.html")
