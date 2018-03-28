from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publish_date = models.DateTimeField(verbose_name='Giriş Tarihi', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # post uygulamasındaki detail url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:detail', kwargs={'id': self.id})
