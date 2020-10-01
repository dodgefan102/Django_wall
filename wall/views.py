from django.shortcuts import render, redirect
from .models import Posts, Comments
from login.models import Users
from django.contrib import messages

# Create your views here.
def index(request):
    if "user_id" not in request.session:
        messages.error(request, "You must be logged in to do that!")
        return redirect('/')
    else:
        context={
            'user':Users.objects.get(id=request.session['user_id']),
            'action':request.session['action'],
            'posts':reversed(Posts.objects.all())
        }
        return render(request, 'wall.html', context)

def postblog(request):
    Posts.objects.create(
        text=request.POST['text'],
        user=Users.objects.get(id=request.POST['user_id'])
    )
    return redirect('/wall')

def comment(request):
    Comments.objects.create(
        text=request.POST['text'],
        user=Users.objects.get(id=request.session['user_id']),
        post=Posts.objects.get(id=request.POST['blog_id'])
    )
    return redirect('/wall')

def comdelete(request):
    Comments.objects.get(id=request.POST['com_id']).delete()
    return redirect('/wall')

def postdelete(request):
    Posts.objects.get(id=request.POST['post_id']).delete()
    return redirect('/wall')