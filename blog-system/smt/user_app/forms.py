from django.forms import ModelForm

from user_app.models import Manager, Supervisor, AssistanceSupervisor, Cleaner, ShopOwner


class ManagerForm(ModelForm):

    class Meta:
        model = Manager
        fields = '__all__'


class SupervisorForm(ModelForm):

    class Meta:
        model = Supervisor
        fields = '__all__'


class AsupervisorForm(ModelForm):

    class Meta:
        model = AssistanceSupervisor
        fields = '__all__'


class Cleaners(ModelForm):

    class Meta:
        model = Cleaner
        fields = '__all__'


class ShopOwnerForm(ModelForm):

    class Meta:
        model = ShopOwner
        fields = '__all__'



