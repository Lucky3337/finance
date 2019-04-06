from django.views.generic import TemplateView, DetailView, RedirectView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Post, Index


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'main_app/base.html'
    context_object_name = 'content'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = dict()
        context['categories'] = Index.get_categories()
        print(str(context))
        return context


class PostView(LoginRequiredMixin, DetailView):
    template_name = 'main_app/post.html'
    model = Post


