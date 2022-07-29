from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from smt_app.forms import UserForm
from smt_app.models import User


class UserRegistration(CreateView):
    template_name = 'main.html'
    model = User
    form_class = UserForm
    success_url = "login/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        if user.roll == "MANAGER":
            return redirect("manager")
        elif user.roll == "SUPERVISOR":
            return redirect("supervisor")
        elif user.roll == "ASSISTANT SUPERVISOR":
            return redirect("asupervisor")
        elif user.roll == "CLEANER":
            return redirect("cleaner")
        elif user.roll == "SHOP":
            return redirect("shopmanager")
        elif user.roll == "SHOP OWNER":
            return redirect("shopowner")

        return super(UserRegistration, self).form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ['address','phone_no', 'roll']
    template_name = 'main.html'

    def get_success_url(self):
        if self.request.user.roll == 'MANAGER':
            return reverse('detailmanager', kwargs={"pk": self.request.user.category_id.id})

        if self.request.user.roll == 'SUPERVISOR':
            return reverse('detailsupervisor', kwargs={"pk": self.request.user.category_id.id})

        if self.request.user.roll == 'ASSISTANT SUPERVISOR':
            return reverse('detailasupervisor', kwargs={"pk": self.request.user.category_id.id})

        if self.request.user.roll == 'CLEANER':
            return reverse('detailmanager', kwargs={"pk": self.request.user.category_id.id})

        if self.request.user.roll == 'SHOP':
            return reverse('detailsupervisor', kwargs={"pk": self.request.user.category_id.id})

        if self.request.user.roll == 'SHOP OWNER':
            return reverse('detailsupervisor', kwargs={"pk": self.request.user.category_id.id})


class UserLogin(LoginView):
    template_name = 'main.html'

    def form_valid(self, form):

        super(UserLogin, self).form_valid(form)
        user = form.get_user()
        if user.roll == "MANAGER":
            return HttpResponseRedirect(reverse('detailmanager', kwargs={"pk": self.request.user.category_id}))
        elif user.roll == "SUPERVISOR":
            return HttpResponseRedirect(reverse('detailsupervisor', kwargs={"pk": self.request.user.category_id}))
        elif user.roll == "ASSISTANT SUPERVISOR":
            return HttpResponseRedirect(reverse('detailasupervisor', kwargs={"pk": self.request.user.category_id.id}))
        elif user.roll == "CLEANER":
            return HttpResponseRedirect(reverse('detailcleaner', kwargs={"pk": self.request.user.category_id}))
        # elif user.roll == "SHOP":
        #     return HttpResponseRedirect(reverse('detailshopmanager', kwargs={"pk": self.request.user.category_id}))
        elif user.roll == "SHOP OWNER":
            return HttpResponseRedirect(reverse('detailashopowner', kwargs={"pk": self.request.user.category_id}))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")
