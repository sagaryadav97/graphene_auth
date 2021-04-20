from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import LoginUser


class LoginUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = LoginUser
        fields = ('email', 'name', 'phone')


class LoginUserChangeForm(UserChangeForm):

    class Meta:
        model = LoginUser
        fields = ('email', 'name', 'phone')