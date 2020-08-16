from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/accounts/login/')
def feed(request):
    pictures = Post.objects.all()
    return render(request, 'index.html',{'pictures':pictures})


# @login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user.profile
    pics = Post.objects.filter(profile=current_user).all()
    return render(request, 'profile.html', {'pics':pics})

