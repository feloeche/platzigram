#Django
from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        """form settings."""

        model = Post
        fields =('user','profile','title', 'photo')