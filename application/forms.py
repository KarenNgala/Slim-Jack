from django import forms
from .models import Profile, Post, Rating


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']

class uploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'created_on']

class rateProject(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['interface', 'experience', 'content']