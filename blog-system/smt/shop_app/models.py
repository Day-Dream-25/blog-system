from datetime import datetime

from django.db import models

# Create your models here.

from user_app.models import Supervisor, AssistanceSupervisor, Cleaner


class Tax(models.Model):
    shop_category = models.CharField(max_length=20)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return str(self.shop_category)


class CleanerGroup(models.Model):
    group_name = models.CharField(max_length=20)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null= True, related_name='cleaner_group_supervisor')

    def __str__(self):
        return str(self.group_name)


class Shop(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='shopdetail')
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('smt_app.City', on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey('smt_app.Zone', on_delete=models.CASCADE, null=True)
    electricity_meter = models.IntegerField()
    shop_no = models.IntegerField()
    history = models.ManyToManyField("shop_app.ShopDetail",  related_name='history_shop', blank=True, null=True)

    def __str__(self):
        return str(self.shop_no)


class ShopDetail(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='shop')
    is_status = models.BooleanField("status", default='True')
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    shop_detail = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True )
    shop_name = models.CharField(max_length=20, null=True)
    shop_owner = models.ManyToManyField("user_app.ShopOwner", related_name='shopownershopdetail')
    age = models.IntegerField(null=True)
    category = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('smt_app.City', on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey('smt_app.Zone', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.shop_name)


class CleanerRecord(models.Model):
    date = models.DateField(default=datetime.now().date())
    records = models.BooleanField()
    group = models.ForeignKey(Cleaner, on_delete=models.CASCADE, null=True)
    shop_detail = models.ForeignKey(ShopDetail, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class ShopWorker(models.Model):
    shop_detail = models.ForeignKey(ShopDetail, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class AssignCleanerGroup(models.Model):
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    cleaner_group = models.ForeignKey(CleanerGroup, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.now().date())
    assign_status = models.BooleanField()


class Assigncleanerd(models.Model):
    date= models.DateTimeField(default=datetime.now().date(), null=True)
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    cleaner_group = models.ForeignKey(CleanerGroup, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(ShopDetail, on_delete=models.CASCADE, null=True)
    record = models.BooleanField(null=True)

