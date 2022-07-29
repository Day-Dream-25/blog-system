from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from smt_app.models import User, Manager, Supervisor, AssistanceSupervisor, Cleaner, Shop, ShopDetail, ShopOwner


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password', 'phone_no', 'address', 'roll'
        )


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


class LoginForm(AuthenticationForm):

    class Meta:

        model = User
        fields = ('username', 'password')


class Cleaners(ModelForm):

    class Meta:
        model = Cleaner
        fields = '__all__'


# class ShopDetail(ModelForm):
#
#     class Meta:
#         model = Shop
#         fields = '__all__'


class ShopOwnerForm(ModelForm):

    class Meta:
        model = ShopOwner
        fields = '__all__'






