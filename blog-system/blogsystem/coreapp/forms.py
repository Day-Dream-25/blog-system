
from django.forms import ModelForm

from coreapp.models import Profile, ContactUs


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class ContactUsForm(ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'


