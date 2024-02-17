from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm  # созданная нами модель


# представление к модели BaseRegisterForm
class BaseRegisterView(CreateView):
    # модель формы, которую реализует данный дженерик
    model = User
    # форма, которая будет заполняться пользователем
    form_class = BaseRegisterForm
    # URL для редиректа пользователя после успешного ввода данных в форму
    success_url = '/'
