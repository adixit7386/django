from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import NewFeature as Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages
import sys
# Create your views here.
def index(request):
    # feature1=Feature()
    # feature1.id=10
    # feature1.name="very fast"
    # feature1.details="our services are very fast and quick"
    # feature2=Feature()
    # feature2.id=20
    # feature2.name="very fast"
    # feature2.details="our services are very fast and secure"
    # feature3=Feature()
    # feature3.id=30
    # feature3.name="very fast"
    # feature3.details="our services are very fast and reliable"
    # feature4=Feature()
    # feature4.id=40
    # feature4.name="very fast"
    # feature4.details="our services are very fast and good"
    
    # feature=[feature1,feature2,feature3,feature1]
    feature=Feature.objects.all()
    return render(request,'index.html',{'features':feature})
def counter(request):
    words=request.POST['text']
    counts = len(words.split())
    
    return render(request,'counter.html',{'counts':counts})
def register(request):
    if request.method=='POST':
        # print >>sys.stderr, 'Goodbye, cruel world!'
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        text="Your passwords do not match"
        # return HttpResponse(password2)
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords not same')
            return redirect('register')
        # return HttpResponse(username)
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # return HttpResponse(username)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/',user)
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/') 
        
