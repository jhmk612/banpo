from django import forms
from django.forms import ModelForm, NumberInput
from .models import Post, Comment, Like


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'media', 'content']
        labels={'title':'제목', 'media':'극혐자료', 'content':'내용'}

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        labels={'content':'답글'}

class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
        fields=['rating']
        labels={'rating':'극혐 정도'}





