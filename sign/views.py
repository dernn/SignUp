from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm  # созданная нами модель
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
