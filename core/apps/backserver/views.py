from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, TemplateView, DetailView, ListView

from core.apps.backserver.forms import UserRegistrationForm, UserLoginForm
from core.apps.backserver.models import *

# register and login

class UserRegistrationView(CreateView):

    form_class=UserRegistrationForm
    template_name="register.html"
    context_object_name="form"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
            return render(request, self.template_name, {'form': form})


class UserLoginView(TemplateView):

    form_class = UserLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            print(form.clean())
            username = form.clean()['username']
            password = form.clean()['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
        return render(request, self.template_name, context={'form': form})

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('Login')

class MainPageView(ListView):

    queryset=Method.objects.all()
    template_name="home.html"
    context_object_name="methods"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('Login')
        return super().get(self, request, *args, **kwargs)