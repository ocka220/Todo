from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField


class CustomUserForm(UserCreationForm):
    """
    Форма регистрации нового пользователя
    """
    error_messages = {
        'password_mismatch': "Пароль не одинаков"
    }

    # def clean_username(self):
    #
    #    raise forms.ValidationError('Имя уже зарегистрировано')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            'username': {
                'unique_together': "Другое имя введите",
                'unique':'Другое имя'
            },
            'password2': {
                'password_mismatсh':'Пароль не одинаков',
            }
        }


class LoginForm(forms.Form):
    login = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.TextInput()
    )

    password = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.PasswordInput()
    )
