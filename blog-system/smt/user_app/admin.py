

from django.contrib import admin

# Register your models here.
from user_app.models import Manager, Supervisor, AssistanceSupervisor, Cleaner, ShopOwner

admin.site.register(Manager)
admin.site.register(Supervisor)
admin.site.register(AssistanceSupervisor)
admin.site.register(Cleaner)
admin.site.register(ShopOwner)
