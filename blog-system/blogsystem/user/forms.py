from django.forms import ModelForm

from user.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = "__all__"
        # fields = (
        #     'username', 'email', 'first_name', 'last_name', 'password', 'address'
        # )