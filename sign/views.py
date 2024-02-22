from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic import View
# миксин для проверки наличия прав доступа
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import BaseRegisterForm  # созданная нами модель
# для апгрейда аккаунта до Premium
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# представление к модели BaseRegisterForm
class BaseRegisterView(CreateView):
    # модель формы, которую реализует данный дженерик
    model = User
    # форма, которая будет заполняться пользователем
    form_class = BaseRegisterForm
    # URL для редиректа пользователя после успешного ввода данных в форму
    success_url = '/'


# проверка аутентификации через декоратор
@login_required
def upgrade_me(request):
    # объект текущего пользователя
    user = request.user
    # премиум-группа из модели Group
    premium_group = Group.objects.get(name='premium')
    # проверяем наличие пользователя в группе
    if not request.user.groups.filter(name='premium').exists():
        # и добавляем, в случае его отсутствия
        premium_group.user_set.add(user)
    # перенаправляем пользователя на корневую страницу
    return redirect('/')


# эта вьюха здесь для примера, в приложение нигде не используется
class MyView(PermissionRequiredMixin, View):  # <-- PermissionRequiredMixin : проверка прав доступа
    # соглашение для именования разрешений, [view-add-delete-change]:
    # <app>.<action>_<model>
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>',)  # выдача разрешений
    # для каждого разрешение здесь необходимо выдать такое же в админке