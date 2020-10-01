from django.shortcuts import render,redirect
from .models import Users
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'index.html')

def reg(request):
    e=Users.objects.regVals(request.POST)
    if len(e)==0:
        pw=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode()
        Users.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            password=pw
        )
        request.session['action']='registered'
        request.session['user_id']=Users.objects.last().id
        return redirect('/wall')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/')

def log(request):
    e=Users.objects.logVals(request.POST)
    if len(e)==0:
        request.session['user_id']=Users.objects.get(email=request.POST['email']).id
        request.session['action']='logged in'
        return redirect('/wall')
    else:
        for i in e.values():
            messages.error(request,i)
        return redirect('/')

def success(request):
    context={
        'user':Users.objects.get(id=request.session['user_id']),
        'action':request.session['action']
    }
    return render(request,'success.html',context)

def out(request):
    request.session.clear()
    return redirect('/')