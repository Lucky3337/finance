from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    template_name = 'main_app/content.html'
    # redirect_field_name = 'redirect_to'