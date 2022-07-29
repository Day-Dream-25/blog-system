from django.contrib import admin

# Register your models here.
from shop_app.models import Shop, Tax, ShopDetail, CleanerRecord, ShopWorker, CleanerGroup, AssignCleanerGroup, \
    Assigncleanerd

admin.site.register(Shop)
admin.site.register(ShopDetail)
admin.site.register(Tax)
admin.site.register(CleanerGroup)
admin.site.register(CleanerRecord)
admin.site.register(ShopWorker)
admin.site.register(AssignCleanerGroup)
admin.site.register(Assigncleanerd)
