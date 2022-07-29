from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from coreapp.models import Profile
from user.forms import UserForm
from user.models import User


class UserRegistration(CreateView):
    template_name = 'user/registration.html'
    model = User
    form_class = UserForm
    success_url = "login/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return HttpResponseRedirect(self.success_url)


class UserUpdateView(UpdateView):
    model = Profile   # User
    fields = ['gender', 'dob']
    template_name = 'core.html'

    def get_success_url(self):
        return reverse('blogs_list')


class UserLogin(LoginView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm
    success_url = 'blog_list'

    def get_success_url(self):
        return reverse('blogs_list')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")





