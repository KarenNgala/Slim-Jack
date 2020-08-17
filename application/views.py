from django.shortcuts import render, redirect
from .models import Post, Profile, Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditProfile, uploadForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def feed(request):
    pictures = Post.objects.all()
    return render(request, 'index.html',{'pictures':pictures})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user.profile
    pics = Post.objects.filter(profile=current_user).all()
    return render(request, 'profile.html', {'pics':pics})


@login_required(login_url='/accounts/login/')
def project(request, id):
    current_user = request.user.profile
    post = Post.objects.filter(id=id).all()
    rate = Rating.objects.filter(post=post).all()
    return render(request, 'project.html', {'post':post, 'rate':rate})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
    else:
        form = EditProfile()
    return render(request, 'django_registration/registration_complete.html', {'form':form})
    

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('feed')
    else:
        form = uploadForm()
    return render(request, 'upload.html', {'form':form})