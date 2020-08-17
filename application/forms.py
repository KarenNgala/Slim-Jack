from django import forms
from .models import Profile, Post


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']

class uploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'created_on']
