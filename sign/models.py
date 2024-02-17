# UserCreationForm базовая форма для создания пользователя
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    # добавляем в форму-наследницу новые поля
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    # и передаем в Meta-класс
    class Meta:
        # в модели User(AbstractUser) поля почта, имя и фамилия есть по умолчанию
        model = User
        fields = ("username",  # поля "из коробки" UserCreationForm
                  "first_name",  # поля модели User(AbstractUser)
                  "last_name",  # поля модели User(AbstractUser)
                  "email",  # поля модели User(AbstractUser)
                  "password1",  # поля "из коробки" UserCreationForm
                  "password2",)  # поля "из коробки" UserCreationForm
