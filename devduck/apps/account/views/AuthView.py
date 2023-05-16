from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse

from devduck.apps.account.models import User
from devduck.apps.blog.models import Post
from devduck.apps.account.forms.AuthForm import UserCreationForm, UserChangeForm

# Create your views here.


class LoginView(LoginView):

    template_name = 'auth/auth.html'
    success_url = reverse_lazy('blog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['button_link'] = 'account:register'
        context['button'] = 'Cadastre-se'
        context['action'] = 'login'
        return context

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)


class LogoutView(LogoutView):

    template_name = 'home/home.html'


class RegisterView(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = 'auth/auth.html'
    success_url = reverse_lazy('blog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastre-se'
        context['button_link'] = 'account:login'
        context['button'] = 'Login'
        context['action'] = 'register'
        return context

    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        return super().form_valid(form)


class ProfileView(ListView):

    template_name = 'profile/profile.html'
    context_object_name = 'data_user'
    paginate_by = 3

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username:
            user = User.objects.get(username=username)
        else:
            user = self.request.user

        return Post.objects.filter(id_user=user.id)
