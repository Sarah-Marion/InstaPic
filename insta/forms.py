from .models import Image
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required. Kindly input a valid email address' )

    class Meta:
        model = User
        fields = ('username', 'email', '1st_password', '2nd_password')
        unique_together = ('email')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['1st_password'].widget.attrs['placeholder'] = 'Password'
        self.fields['2nd_password'].widget.attrs['placeholder'] = 'Confirm your Password'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_name', 'image', 'image_caption')


    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.fields['image_name'].widget.attrs['placeholder'] = 'Kindly input an image name'
        self.fields['image'].widget.attrs['placeholder'] = 'Pick a Pic'
        self.fields['image_caption'].widget.attrs['placeholder'] = 'Kindly add a Caption to the image'