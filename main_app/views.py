from django.shortcuts import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main_app/base.html'