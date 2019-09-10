"""Posts forms."""

# django
from django import forms

# models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post models form"""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
