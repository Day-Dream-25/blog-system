from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from smt_app.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password', 'phone_no', 'address', 'roll'
        )


class LoginForm(AuthenticationForm):

    class Meta:

        model = User
        fields = ('username', 'password')




# class ShopDetail(ModelForm):
#
#     class Meta:
#         model = Shop
#         fields = '__all__'







