from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    # Bu form modeli, Post modelimiz icimn yapılıyor, bu sebeple referans olarak Post modelimizi veriyoruz
    class Meta:
        model = Post
        # Formda olmasını istediğimiz fieldları belirtiyoruz. Publish_date otomatik dolduğundan eklemiyoruz.
        fields = [
            'title',
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # Formda olmasını istediğimiz fieldları belirtiyoruz.
        fields = [
            'name',
            'content',
        ]