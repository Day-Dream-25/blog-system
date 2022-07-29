from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from smt_app.forms import UserForm, ManagerForm, SupervisorForm, Cleaners
    # ShopManager, ShopOwner
from smt_app.models import User, Manager, Supervisor, AssistanceSupervisor, Cleaner
    # Shop, Shop_Detail


class UserRegistration(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserForm
    success_url = "login/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        # import pdb;pdb.set_trace()
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
        elif user.roll == "SHOP":
            return HttpResponseRedirect(reverse('detailshopmanager', kwargs={"pk": self.request.user.category_id}))
        elif user.roll == "SHOP OWNER":
            return HttpResponseRedirect(reverse('detailashopowner', kwargs={"pk": self.request.user.category_id}))


class ManagerView(CreateView):
    template_name = 'main.html'
    model = Manager
    form_class = ManagerForm
    success_url = "/login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ManagerListView(ListView):
    model = Manager
    template_name = 'school_home.html'


class ManagerUpdateView(UpdateView):
    model = Manager
    fields = '__all__'
    template_name = 'main.html'

    def put(self, *args, **kwargs):
        import pdb
        pdb.set_trace()

    def get_success_url(self):
        return reverse('updateschool', kwargs={"pk": self.request.user.category_id.id})


class ManagerDeleteView(DeleteView):
    template_name = 'main.html'


class ManagerDetailView(DetailView):
    model = Manager
    template_name = 'Manager/manager_detail.html'


class SupervisorCreateView(CreateView):
    template_name = 'main.html'
    model = Supervisor
    form_class = SupervisorForm
    success_url = "/login/"


class SupervisorListView(ListView):
    model = Supervisor
    template_name = 'supervisor/supervisor_home.html'

    def get_queryset(self):
        return Supervisor.objects.filter(manager_id=self.request.user.category_id)


class SupervisorUpdateView(UpdateView):
    model = Supervisor
    fields = '__all__'
    template_name = 'main.html'
    success_url = "/teacherdetail/"

    def get_success_url(self):
        # import pdb
        # pdb.set_trace()
        if not self.request.GET.get('school'):
            return reverse('updateteacher', kwargs={"pk": self.request.user.category_id})
        return self.success_url

        # return 'updateteacher' + '/' + str(self.request.user.category_id)


class SupervisorDeleteView(DeleteView):
    model = Supervisor
    template_name = 'delete.html'

    def get_success_url(self):
        # return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})

        return 'detailschool' + '/' + str(self.request.user.category_id)


class SupervisorDetailView(DetailView):
    model = Supervisor
    template_name = 'supervisor/supervisor_detail.html'


class AssSupervisorView(CreateView):
    template_name = 'main.html'
    model = AssistanceSupervisor
    # form_class = StudentForm
    fields = '__all__'
    success_url = "/login/"


class AssSupervisorListView(ListView):
    model = AssistanceSupervisor
    template_name = 'ass_supervisor/ass_supervisor_home.html'

    def get_queryset(self, **kwargs):
        return AssistanceSupervisor.objects.filter(supervisor_id=self.kwargs.get('pk'))

    # def get_queryset(self):
    #     # import pdb;pdb.set_trace()
    #     if self.request.user.roll == "MANAGER":
    #         return AssistanceSupervisor.objects.filter(manager_id=self.request.user.category_id)
    #     if self.request.user.roll == "SUPERVISOR":
    #         return AssistanceSupervisor.objects.filter(supervisor_id=self.request.user.category_id)


class AssSupervisorUpdateView(UpdateView):
    model = AssistanceSupervisor
    # fields = ('school',  'birthdate', 'standard')
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):

        if self.request.user.roll == 'STUDENT':
            return reverse('updatestudent', kwargs={"pk": self.request.user.category_id.id})
            # return HttpResponseRedirect(reverse('updatestudent', kwargs={"pk": self.request.user.category_id.id}))
            # return 'updatestudent' + '/' + str(self.request.user.category_id)
        if self.request.user.roll == 'SCHOOL':
            return reverse('updateschool', kwargs={"pk": self.request.user.category_id.id})
            # return 'updateschool' + '/' + str(self.request.user.category_id)


class AssSupervisorDeleteView(DeleteView):
    model = AssistanceSupervisor
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})

        # return 'detailschool' + '/' + str(self.request.user.category_id)


class AssSupervisorDetailView(DetailView):
    model = AssistanceSupervisor
    template_name = 'ass_supervisor/ass_supervisor_detail.html'

#
class CleanerView(CreateView):
    template_name = 'main.html'
    model = Cleaner
    form_class = Cleaners
    success_url = "/login/"


class CleanerListView(ListView):
    model = Cleaner
    template_name = 'cleaner/cleaner_home.html'

    def get_queryset(self):
        return Supervisor.objects.filter(manager_id=self.request.user.category_id)


class CleanerUpdateView(UpdateView):
    model = Cleaner
    fields = '__all__'
    template_name = 'main.html'
    success_url = "/teacherdetail/"

    def get_success_url(self):
        # import pdb
        # pdb.set_trace()
        if not self.request.GET.get('school'):
            return reverse('updateteacher', kwargs={"pk": self.request.user.category_id})
        return self.success_url

        # return 'updateteacher' + '/' + str(self.request.user.category_id)


class CleanerDeleteView(DeleteView):
    model = Cleaner
    template_name = 'delete.html'

    def get_success_url(self):
        # return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})

        return 'detailschool' + '/' + str(self.request.user.category_id)


class CleanerDetailView(DetailView):
    model = Cleaner
    template_name = 'cleaner/cleaner_detail.html'

#
# class Shop_ManagerView(CreateView):
#     template_name = 'main.html'
#     model = Shop_Detail
#     form_class = ShopManager
#     success_url = "/login/"
#
#
# class Shop_ManagerListView(ListView):
#     model = Shop_Detail
#     template_name = 'shop manager/shopmanager_home.html'
#
#     def get_queryset(self,**kwargs):
#         # import pdb;pdb.set_trace()
#         return Shop_Detail.objects.filter(ass_supervisor_id=self.kwargs.get('pk'))
#
#
# class Shop_ManagerUpdateView(UpdateView):
#     model = Shop
#     fields = '__all__'
#     template_name = 'main.html'
#     success_url = "/teacherdetail/"
#
#     def get_success_url(self):
#         # import pdb
#         # pdb.set_trace()
#         if not self.request.GET.get('school'):
#             return reverse('updateteacher', kwargs={"pk": self.request.user.category_id})
#         return self.success_url
#
#         # return 'updateteacher' + '/' + str(self.request.user.category_id)
#
#
# class Shop_ManagerDeleteView(DeleteView):
#     model = Shop_Detail
#     template_name = 'delete.html'
#
#     def get_success_url(self):
#         # return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})
#
#         return 'detailschool' + '/' + str(self.request.user.category_id)
#
#
# class Shop_ManagerDetailView(DetailView):
#     model = Shop_Detail
#     template_name = 'shop manager/shopmanager_detail.html'
#
#
# class Shop_OwnerView(CreateView):
#     template_name = 'main.html'
#     model = Shop
#     form_class = ShopOwner
#     success_url = "/login/"
#
#
# class Shop_OwnerListView(ListView):
#     model = Shop
#     template_name = 'supervisor_home.html'
#
#     def get_queryset(self):
#         return Supervisor.objects.filter(manager_id=self.request.user.category_id)
#
#
# class Shop_OwnerUpdateView(UpdateView):
#     model = Shop
#     fields = '__all__'
#     template_name = 'main.html'
#     success_url = "/teacherdetail/"
#
#     def get_success_url(self):
#         # import pdb
#         # pdb.set_trace()
#         if not self.request.GET.get('school'):
#             return reverse('updateteacher', kwargs={"pk": self.request.user.category_id})
#         return self.success_url
#
#         # return 'updateteacher' + '/' + str(self.request.user.category_id)
#
#
# class Shop_OwnerDeleteView(DeleteView):
#     model = Shop
#     template_name = 'delete.html'
#
#     def get_success_url(self):
#         # return reverse('detailschool', kwargs={"pk": self.request.user.category_id.id})
#
#         return 'detailschool' + '/' + str(self.request.user.category_id)
#
#
# class Shop_OwnerDetailView(DetailView):
#     model = Shop
#     template_name = 'shop_owner/shopowner_detail.html'
#
