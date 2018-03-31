
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=150, verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    publish_date = models.DateTimeField(verbose_name='Giriş Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # post uygulamasındaki detail url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        # Aslında {% url 'post_app:detail id=self.id' %} yani /post/self.id/update değeri döner
        return reverse('post_app:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        # post uygulamasındaki create url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:create')

    def get_update_url(self):
        # post uygulamasındaki update url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        # post uygulamasındaki delete url i ni id parametresini vererek çağırdığımızı belirtiyoruz.
        return reverse('post_app:delete', kwargs={'slug': self.slug})

    # Title bilgisi slugify ediliyor ve veri tabanındaki slug alanları kontrol edilerek unique olması sağlanıyor
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publish_date']
