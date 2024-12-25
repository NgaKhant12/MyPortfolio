from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)


def personal_info(request):
    context = {}
    
    return render(request,"personal_info.html",context)

def projects(request):
    context = {}
    
    return render(request,"projects.html",context)

def contact(request):
    context = {}
    
    return render(request,"contact.html",context)
