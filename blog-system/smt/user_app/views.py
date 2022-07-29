from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from user_app.forms import ManagerForm, SupervisorForm, Cleaners, ShopOwnerForm
from user_app.models import Manager, Supervisor, AssistanceSupervisor, Cleaner, ShopOwner


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

    def get_success_url(self):
        return reverse('detailmanager', kwargs={"pk": self.request.user.category_id.id})


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


@method_decorator(login_required, name='dispatch')
class SupervisorListView(ListView):
    model = Supervisor
    template_name = 'supervisor/supervisor_home.html'

    def get_queryset(self):
        return Supervisor.objects.filter(manager_id=self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class SupervisorUpdateView(UpdateView):
    model = Supervisor
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):

        return reverse('supervisorlist', kwargs={"pk": self.request.user.category_id})


class SupervisorDeleteView(DeleteView):
    model = Supervisor
    template_name = 'delete.html'


@method_decorator(login_required, name='dispatch')
class SupervisorDetailView(DetailView):
    model = Supervisor
    template_name = 'supervisor/supervisor_detail.html'


class AssSupervisorView(CreateView):
    template_name = 'main.html'
    model = AssistanceSupervisor
    fields = '__all__'
    success_url = "/login/"


@method_decorator(login_required, name='dispatch')
class AssSupervisorListView(ListView):
    model = AssistanceSupervisor
    template_name = 'ass_supervisor/ass_supervisor_home.html'

    def get_queryset(self, **kwargs):
        # self.request.session.set('manger_id', '1')
        return AssistanceSupervisor.objects.filter(supervisor_id=self.kwargs.get('pk'))

    # def get_queryset(self):
    #     # import pdb;pdb.set_trace()
    #     if self.request.user.roll == "MANAGER":
    #         return AssistanceSupervisor.objects.filter(manager_id=self.request.user.category_id)
    #     if self.request.user.roll == "SUPERVISOR":
    #         return AssistanceSupervisor.objects.filter(supervisor_id=self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class AssSupervisorUpdateView(UpdateView):
    model = AssistanceSupervisor
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('asupervisorlist', kwargs={"pk": self.request.user.category_id.id})


class AssSupervisorDeleteView(DeleteView):
    model = AssistanceSupervisor
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('detailsupervisor', kwargs={"pk": self.request.user.category_id.id})


@method_decorator(login_required, name='dispatch')
class AssSupervisorDetailView(DetailView):
    model = AssistanceSupervisor
    template_name = 'ass_supervisor/ass_supervisor_detail.html'


class CleanerView(CreateView):
    template_name = 'main.html'
    model = Cleaner
    form_class = Cleaners
    success_url = "/login/"


@method_decorator(login_required, name='dispatch')
class CleanerListView(ListView):
    model = Cleaner
    template_name = 'cleaner/cleaner_home.html'

    def get_queryset(self, **kwargs):
        return Cleaner.objects.filter(cleaner_group_id=self.kwargs.get('pk'))


@method_decorator(login_required, name='dispatch')
class CleanerUpdateView(UpdateView):
    model = Cleaner
    fields = '__all__'
    template_name = 'main.html'
    success_url = "/teacherdetail/"

    def get_success_url(self):
        return reverse('updatecleaner', kwargs={"pk": self.request.user.category_id.id})


class CleanerDeleteView(DeleteView):
    model = Cleaner
    template_name = 'delete.html'

    def get_success_url(self):
        return 'detailcleaner' + '/' + str(self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class CleanerDetailView(DetailView):
    model = Cleaner
    template_name = 'cleaner/cleaner_detail.html'


class Shop_OwnerView(CreateView):
    template_name = 'main.html'
    model = ShopOwner
    form_class = ShopOwnerForm
    success_url = "/login/"


@method_decorator(login_required, name='dispatch')
class Shop_OwnerListView(ListView):
    model = ShopOwner
    template_name = 'supervisor_home.html'

    def get_queryset(self):
        return Supervisor.objects.filter(manager_id=self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class Shop_OwnerUpdateView(UpdateView):
    model = ShopOwner
    fields = '__all__'
    template_name = 'main.html'
    success_url = "/updateshopowner/"

    def get_success_url(self):
        return reverse('updateshopowner', kwargs={"pk": self.request.user.category_id.id})


@method_decorator(login_required, name='dispatch')
class Shop_OwnerDeleteView(DeleteView):
    model = ShopOwner
    template_name = 'delete.html'

    def get_success_url(self):
        return 'detailschool' + '/' + str(self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class Shop_OwnerDetailView(DetailView):
    model = ShopOwner
    template_name = 'shop_owner/shopowner_detail.html'
