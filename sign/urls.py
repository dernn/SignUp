from django.urls import path
# представления "из коробки"
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView

# добавляем представления в файл конфигурации URL
urlpatterns = [
    path('login/',
         # для представлений "из коробки" указываем шаблон
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),
]
