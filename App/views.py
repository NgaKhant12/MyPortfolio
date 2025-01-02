from django.shortcuts import redirect, render

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from MyPortfolio import settings

from.models import ContactInfo
from .forms import Contact_Info_Form

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
    
    if request.method == "POST":
        uname = request.POST.get("name")
        uemail = request.POST.get("email")
        usubject = request.POST.get("subject")
        umessage = request.POST.get("text_area")

        form = Contact_Info_Form(
            {'name':uname,
             'email':uemail,
             "subject":usubject,
             "message": umessage}
        )
        
        # form = Contact_Info_Form(request.POST)

        # email = form['email'].value()  # contact form မှာ ထည့်လိုက်တဲ့ email ကို ယူထားတယ်။ 
        # send_welcome_email(email) #send_welcome_email function ကို email argument ထည့်ပေးပြီး email ပို့ခိုင်းလိုက်တယ်။
        if form.is_valid():
            form.save()
            redirect("/")
    else:
        form = Contact_Info_Form()
    
    
    context = {"form":form}
    
    return render(request,"contact.html",context)

def service(request):
    context = {}
    
    return render(request,"service.html",context)


def send_welcome_email(recevier_email,uname):
    subject = "Welcome to Our Service"
    message = "Hello {%s}, /n Thank you for sending me an email. I'm so glad to have you! Since you recognize My Portfolio ",uname
    recipient_list = [recevier_email]  # လက်ခံမယ့် email ၊ list နဲ့ မဖြစ်မနေထားရမယ်။
    from_email = settings.EMAIL_HOST_USER
    
    send_mail(subject, message, from_email, recipient_list)


  # သင့် function ကို import

def send_email_view(request):
    send_welcome_email()
    return HttpResponse("Email Sent Successfully!")
