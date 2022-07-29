from django.contrib import admin

# Register your models here.
from smt_app.models import User, Manager, Supervisor, AssistanceSupervisor, Cleaner, Shop, Tax, ShopDetail, City, Zone, \
    ShopOwner, CleanerRecord, ShopWorker, CleanerGroup

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Supervisor)
admin.site.register(AssistanceSupervisor)
admin.site.register(Cleaner)
admin.site.register(Shop)
admin.site.register(ShopDetail)
admin.site.register(Tax)
admin.site.register(City)
admin.site.register(Zone)
admin.site.register(CleanerGroup)
admin.site.register(ShopOwner)
admin.site.register(CleanerRecord)
admin.site.register(ShopWorker)




