from django.shortcuts import render, redirect
from .models import Post, Profile, Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditProfile, uploadForm, rateProject
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer, ProfileSerializer


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
    project = Post.objects.filter(id=id).all()
    rate = Rating.objects.filter(post=id).first()
    if Rating.objects.filter(user=current_user, post=id).first() is None : #user has not voted
        if request.method == 'POST':
            form = rateProject(request.POST)
            if form.is_valid():
                rate = form.save(commit=False)
                rate.user = current_user
                rate.post = project
                rate.save()
            return redirect('project')
        else:
            form = rateProject()
        return render(request, 'project.html', {'post':project, 'rate':rate, 'form':form})


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


def search(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        res = Post.search_project(search_term)
        return render(request, 'search.html', {'res':res})
    else:
        return render(request, 'index.html')


class ProfileList(APIView):
    def get(self, request, format=None):
        all_users = Profile.objects.all()
        serializers = ProfileSerializer(all_users, many=True)
        return Response(serializers.data)


class PostList(APIView):
    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data)