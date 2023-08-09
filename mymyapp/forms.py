from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)