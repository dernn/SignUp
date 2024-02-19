# UserCreationForm базовая форма для создания пользователя
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Кастомизируем форму регистрации SignupForm, которую предоставляет пакет allauth,
# чтобы при успешном прохождении регистрации добавлять пользователя к базовой группе
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
# Cрипты, относящиеся к формам, лучше хранить в отдельном файле forms.py,
# но для нас сейчас это не является принципиальным.
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


# наследуем и переопределяем SignupForm
class BasicSignupForm(SignupForm):
    # переопределим метод save
    def save(self, request):
        # вызываем метод класса-родителя
        user = super(BasicSignupForm, self).save(request)
        # получаем объект модели группы basic
        basic_group = Group.objects.get(name='basic')
        # user_set возвращаем список пользователей группы,
        # add(user) добавляет нового пользователя в список
        basic_group.user_set.add(user)
        return user
