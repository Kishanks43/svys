from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from home.models import Add 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render (request,'index.html')
     
    # return HttpResponse("This is Homepage ")  

def about(request):
    return render (request,'about.html')
    #return HttpResponse("This is Aboutpage ")  

def add_entry(request):

            

    if request.method == "POST" :
        
        try:
            name=request.POST.get("name")
            shop=request.POST.get("shop")
            other=request.POST.get("other")
            type=request.POST.get("type")
            amount=request.POST.get("amount")
            location=request.POST.get("location")
            reference=request.POST.get("reference")
            city=request.POST.get("city")
            state=request.POST.get("state")
            pin=request.POST.get("pin")
            print(f"Received data: name={name}, shop={shop},type={type}, location={location}, amount={amount}, reference={reference},other={other},city={city}, state={state}, pin={pin}")


            Add.objects.create(name=name,shop=shop,type=type,other=other,location=location,amount=amount,reference=reference,city=city,state=state,pin=pin,date=datetime.today())

            messages.success(request,"Your entry has been submitted...")
        except Exception as e :
            messages.error(request, "There was an error submitting your entry.")
            print(f"Error: {e}")

    

    return render (request,'services.html')


#@login_required
def services(request):
    print(f"User: {request.user.username}")

    if request.user.is_authenticated :
        print(f"User {request.user.username} is authenticated.")
        
        return render (request,'services.html')
        
    
    else:
        print ("User is not authenticated")
        return redirect("/login")

    

    
   # return HttpResponse('This is Services Page ')

def loginuser(request):


    user=request.user.username
    if request.user.is_authenticated :
        return redirect("/services")
    
    if request.method == "POST":
        #check if user has entered correct credentials
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            print(f"User {username} logged in successfully.")  # Debug output

            return redirect("/services")
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid username or password.")
            
    
    
    return render (request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect ("/login")


def contact(request):

    if request.method == "POST" :
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        descr=request.POST.get("descr")
        contact=Contact(name=name,email=email,phone=phone,descr=descr,date=datetime.today())
        contact.save()
        messages.success(request, """Thank You for contacting us...
                          Our team will revert to you shortly..""")


    return render (request,'contact.html')
    #return HttpResponse("This is Contact Page ")

    
#@login_required()


