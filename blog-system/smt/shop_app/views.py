from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView
from shop_app.forms import ShopForm, ShopDetailForm, CleanerGroupForm, ShopWorkerForm, CleanerRecordForm, \
    AssignCleanerRecordForm, AssignCleanerRecordsownerForm, AssignCleanerRecordAsupervisorForm, \
    AssignCleanerRecordsupervisorForm
from shop_app.models import Shop, ShopDetail, CleanerGroup, ShopWorker, CleanerRecord, AssignCleanerGroup, \
    Assigncleanerd


class ShopView(CreateView):
    template_name = 'main.html'
    model = Shop
    form_class = ShopForm
    success_url = "/detailmanager/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('detailmanager', kwargs={"pk": self.request.user.category_id})


@method_decorator(login_required, name='dispatch')
class ShopListView(ListView):
    model = Shop
    template_name = 'Shop/shop_home.html'

    # def get_queryset(self, **kwargs):
    #     # import pdb;pdb.set_trace()
    #     return Shop.objects.filter(id=self.kwargs.get('pk'))

    # def get_queryset(self, **kwargs):
    #     return Shop.objects.filter(id=self.kwargs.get('pk'))

    def get_queryset(self, **kwargs):
        print("\n\n\n\n")
        print('>>>>>>>>>>>>>>', self.request.session)
        print("\n\n\n\n")
        return Shop.objects.filter(ass_supervisor_id=self.kwargs.get('pk'))


@method_decorator(login_required, name='dispatch')
class ShopUpdateView(UpdateView):
    model = Shop
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('shoplist', kwargs={"pk": self.request.user.category_id})


class ShopDeleteView(DeleteView):
    model = Shop
    template_name = 'delete.html'

    def get_success_url(self):
        return 'shoplist' + '/' + str(self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class ShopDetailView(DetailView):
    model = Shop
    template_name = ''


class ShopDetailCreateView(CreateView):
    template_name = 'main.html'
    model = ShopDetail
    form_class = ShopDetailForm
    success_url = "/login/"

    def form_valid(self, form):
        assistant_supervisor = form.cleaned_data['ass_supervisor']
        shop_count = ShopDetail.objects.filter(ass_supervisor_id=assistant_supervisor).count()
        # import pdb;pdb.set_trace()

        if shop_count <= 15:
            shop = form.cleaned_data['shop_detail']
            shop_details = ShopDetail.objects.filter(shop_detail_id=shop)

            ShopDetail.objects.filter(shop_detail_id=shop).update(is_status=False)

            for shop_detail in shop_details:
                shop.history.add(shop_detail)
                shop.save()
            form.save()
            return redirect('login')
        return HttpResponse("please choose another assistanat")


@method_decorator(login_required, name='dispatch')
class ShopDetailListView(ListView):
    model = ShopDetail
    template_name = 'shop_detail/shopDetail_home.html'

    def get_queryset(self, **kwargs):
        return ShopDetail.objects.filter(ass_supervisor_id=self.kwargs.get('pk'))


# @method_decorator(login_required, name='dispatch')
class ShopDetailUpdateView(UpdateView):
    model = ShopDetail
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('shopdetaillist', kwargs={"pk": self.request.user.category_id})
    # def get_success_url(self):
    #     return reverse( 'shopdetailupdate' + '/' + str(self.request.user.category_id))
    # def get_success_url(self, **kwargs):
    #     return 'shopdetailupdate', kwargs="pk": self.request.user.category_id.id


class ShopDetailDeleteView(DeleteView):
    model = ShopDetail
    template_name = 'delete.html'

    def get_success_url(self):
        return 'shopdetaillist' + '/' + str(self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class ShopDetailsView(DetailView):
    model = ShopDetail
    template_name = 'shop_detail/shopdetail_detail.html'

    # def get_queryset(self, **kwargs):
    #     # import pdb;pdb.set_trace()
    #     return ShopDetail.objects.filter(ass_supervisor_id=self.kwargs.get('pk'))


class CleanerGroupView(CreateView):
    template_name = 'main.html'
    model = CleanerGroup
    form_class = CleanerGroupForm
    success_url = "/login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CleanerGroupListView(ListView):
    model = CleanerGroup
    template_name = 'cleaner group/cleanergroup_detail.html'


@method_decorator(login_required, name='dispatch')
class CleanerGroupUpdateView(UpdateView):
    model = CleanerGroup
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('cleanergrouplist', kwargs={"pk": self.request.user.category_id})


class CleanerGroupDeleteView(DeleteView):
    model = CleanerGroup
    template_name = 'delete.html'

    def get_success_url(self):
        return 'cleanergrouplist' + '/' + str(self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class CleanerGroupDetailView(DetailView):
    model = CleanerGroup
    template_name = 'Manager/manager_detail.html'


class ShopWorkerView(CreateView):
    template_name = 'main.html'
    model = ShopWorker
    form_class = ShopWorkerForm
    success_url = "/shopworkerlist/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('shopworkerlist' + '/' + str(self.request.user.category_id.pk))

    def get_success_url(self):
        return reverse('shopworkerlist', kwargs={"pk": self.request.user.category_id})


@method_decorator(login_required, name='dispatch')
class ShopWorkerListView(ListView):
    model = ShopWorker
    template_name = 'shop_worker/shopworker_detail.html'
    # success_url = reverse'/shopworkerlist/'

    def get_queryset(self, **kwargs):
        return ShopWorker.objects.filter(shop_detail_id=self.kwargs.get('pk'))

    def get_success_url(self):
        import pdb;pdb.set_trace()
        return reverse('shopworkerlist', kwargs={"pk": self.request.user.category_id.id})
        # return reverse('shopworkerlist' + '/' + str(self.request.user.category_id))


@method_decorator(login_required, name='dispatch')
class ShopWorkerUpdateView(UpdateView):
    model = ShopWorker
    fields = '__all__'
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('shopworkerlist', kwargs={"pk": self.request.user.category_id})


class ShopWorkerDeleteView(DeleteView):
    model = ShopWorker
    template_name = 'delete.html'

    def get_success_url(self):
        return 'shopworkerlist' + '/' + str(self.request.user.category_id)


@method_decorator(login_required, name='dispatch')
class ShopWorkerDetailView(DetailView):
    model = ShopWorker
    template_name = 'Manager/manager_detail.html'


class AttendenceCreateView(CreateView):
    template_name = 'main.html'
    model = CleanerRecord
    form_class = CleanerRecordForm
    success_url = "/login/"

    # def get_success_url(self):
    #     return '/user/shop-owner-detail' + '/' + str(self.request.user.category_id)

    def get_success_url(self):
        return reverse('attendence', kwargs={"pk": self.request.user.category_id.id})

    def form_valid(self, form):
        group = form.cleaned_data['group']
        atttendance = CleanerRecord.objects.filter(date=datetime.now().date(), group=group).count()
        if atttendance >= 1:
            return HttpResponse("attedance is already takken for this shop")
        else:
            form.save()
            return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class AttendenceListView(ListView):
    model = CleanerRecord
    template_name = 'attendence_list.html'


@method_decorator(login_required, name='dispatch')
class historyListView(ListView):
    model = Shop
    template_name = 'basic.html'

    def get_queryset(self, **kwargs):
        return Shop.objects.filter(id=self.kwargs.get('pk'))


class CleaningResult(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        contex = {}
        total = CleanerRecord.objects.filter(date=datetime.now().date()).count()
        attendence = CleanerRecord.objects.filter(date=datetime.now().date(), records=True).count()
        if total:
            result = (attendence*100)/total
            contex['result'] = result
            return contex
        else:
            # messages.add_message(self.request, result, 'A serious error occurred.')
            # return messages.INFO(request,  'Hello world.')
            contex['result'] = "There is no any cleaning attendence record"
            return contex


class AssignCleanerView(CreateView):
    template_name = 'main.html'
    model = AssignCleanerGroup
    form_class = AssignCleanerRecordForm
    success_url = "/detailsupervisor/"


@method_decorator(login_required, name='dispatch')
class AssignCleanerListView(ListView):
    model = AssignCleanerGroup
    template_name = 'assign_cleaner_group/assign_cleaner_group_list.html'


class AssignCleanersupervisorView(CreateView):
    template_name = 'main.html'
    model = Assigncleanerd
    form_class = AssignCleanerRecordsupervisorForm
    success_url = "/detailsupervisor/"


@method_decorator(login_required, name='dispatch')
class AssignCleanersupervisorListView(ListView):
    model = Assigncleanerd
    template_name = 'assign_cleaner_group/supervisor_list.html'


@method_decorator(login_required, name='dispatch')
class AssignCleanerAssupervisorView(UpdateView):
    template_name = 'main.html'
    model = Assigncleanerd
    fields = ('shop',)
    success_url = "/detailsupervisor/"


@method_decorator(login_required, name='dispatch')
class AssignCleanerSownerView(UpdateView):
    template_name = 'main.html'
    model = Assigncleanerd
    fields = ('date', 'record',)
    success_url = "/acowner/"

    def get_success_url(self):
        return reverse('acowner', kwargs={"pk": self.request.user.category_id.id})
    #
    # def form_valid(self, form):
    #     cleaner_group = form.cleaned_data['cleaner_group']
    #     atttendance = Assigncleanerd.objects.filter(date=datetime.now().date(), group=cleaner_group).count()
    #     if atttendance >= 1:
    #         return HttpResponse("attedance is already takken for this shop")
    #     else:
    #         form.save()
    #         return HttpResponseRedirect(self.get_success_url())


