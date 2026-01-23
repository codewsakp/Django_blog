from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#UserCreationForm because we want email to be the part of registtration form

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')