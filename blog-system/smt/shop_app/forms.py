from django.forms import ModelForm

from shop_app.models import Shop, ShopDetail, CleanerGroup, ShopWorker, CleanerRecord, AssignCleanerGroup, \
    Assigncleanerd


class ShopForm(ModelForm):

    class Meta:
        model = Shop
        fields = 'ass_supervisor','city', 'zone', 'electricity_meter', 'shop_no'


class ShopDetailForm(ModelForm):

    class Meta:
        model = ShopDetail
        fields = '__all__'


class CleanerGroupForm(ModelForm):

    class Meta:
        model = CleanerGroup
        fields = '__all__'


class ShopWorkerForm(ModelForm):

    class Meta:
        model = ShopWorker
        fields = '__all__'


class CleanerRecordForm(ModelForm):

    class Meta:
        model = CleanerRecord
        fields = ('date','shop_detail', 'group', 'records')


class AssignCleanerRecordForm(ModelForm):

    class Meta:
        model = AssignCleanerGroup
        fields = '__all__'


class AssignCleanerRecordsupervisorForm(ModelForm):

    class Meta:
        model = Assigncleanerd
        fields = 'date', 'ass_supervisor', 'cleaner_group'


class AssignCleanerRecordAsupervisorForm(ModelForm):

    class Meta:
        model = Assigncleanerd
        fields = ('shop',)


class AssignCleanerRecordsownerForm(ModelForm):

    class Meta:
        model = Assigncleanerd
        fields = ('date', 'record',)
