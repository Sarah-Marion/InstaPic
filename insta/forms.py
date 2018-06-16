from .models import Profile, Image
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm #UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm): 
    """
    Class that creates an Image upload form
    """
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption']


class ProfileUpdateForm(forms.Form):
    """
    classs that creates a Profile update form
    """ 
    username = forms.CharField(label='Username', max_length = 30)
    profile_photo = forms.ImageField(label = 'Image Field') 
    bio = forms.CharField(label='Image Caption', max_length=500)

class CommentForm(forms.ModelForm):
   """
    class that creates the comment form
   """
    class Meta:
        model = Comment
        fields = ['comment']
