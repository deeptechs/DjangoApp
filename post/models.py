from tokenize import blank_re

from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publish_date = models.DateTimeField(verbose_name='Giriş Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # post uygulamasındaki detail url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        # Aslında {% url 'post_app:detail id=self.id' %} yani /post/self.id/update değeri döner
        return reverse('post_app:detail', kwargs={'id': self.id})

    def get_create_url(self):
        # post uygulamasındaki create url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:create')

    def get_update_url(self):
        # post uygulamasındaki update url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:update', kwargs={'id': self.id})

    def get_delete_url(self):
        # post uygulamasındaki delete url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-publish_date']
