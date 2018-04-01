from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Kulanıcı Adı')
    password = forms.CharField(max_length=150, label='Parola', widget=forms.PasswordInput)

    # Her form class ının kendi validation (clean) metodu vardır. Bunları override ederek uyarı mesajlarını verebiliriz.
    # Bu metod formda hata aldığımız zaman çalışır, auteticate hata aldırıp bunun çalışmasını sağlıyor.
    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adı veya Parola Yanlış')
            return super(LoginForm, self).clean()


# Bu formu model formunda türetmek daha uygun çünkü gelen verileri user modeline uygun şekilde gelecek.
class RegisterForm(forms.ModelForm):

    username = forms.CharField(max_length=150, label='Kulanıcı Adı')
    password1 = forms.CharField(max_length=150, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=150, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User

        # User modelinden 3 alan bize lazım onları alıyoruz
        fields = [
            'username',
            'password1',
            'password2',
        ]

    # Form sınıflarının field validation ları için özel metodlar tanımlanır. Clean yazıp alttan tire vererek alan adı
    # yazılarak validation yapılabilir. Bu şekilde form kendini valide eder.
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parolalar eşleşmiyor')
        return password2
