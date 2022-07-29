from django.contrib import admin

# Register your models here.
from coreapp.models import Profile, ContactUs

admin.site.register(Profile)
admin.site.register(ContactUs)

