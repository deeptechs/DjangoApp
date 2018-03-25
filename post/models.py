from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publish_date = models.DateTimeField(verbose_name='Giriş Tarihi')

    def __str__(self):
        return self.title
