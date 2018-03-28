from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    # Bu form modeli, Post modelimiz icimn yapılıyor, bu sebeple referans olarak Post modelimizi veriyoruz
    class Meta:
        model = Post
        # Formda olmasını istediğimiz fieldları belirtiyoruz. Publish_date otomatik dolduğundan eklemiyoruz.
        fields = [
            'title',
            'content',
        ]
