from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'content',
            'excerpt',
            'featured_image',
        ]        