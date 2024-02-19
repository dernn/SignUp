from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        # get_context_data возвращает словарь
        context = super().get_context_data(**kwargs)
        # eists() проверяет, существует ли список filter(name='premium')
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        # возвращаем пополненный ['is_not_premium'] контекст
        return context
