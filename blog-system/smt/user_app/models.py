from django.db import models

# Create your models here.
# from shop_app.models import CleanerGroup
# from smt_app.models import User


class Manager(models.Model):
    user = models.OneToOneField('smt_app.User', on_delete=models.CASCADE, null=True, related_name='manager')
    name = models.CharField(max_length=10)
    city = models.OneToOneField('smt_app.City', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Supervisor(models.Model):
    user = models.OneToOneField('smt_app.User', on_delete=models.CASCADE, null=True, related_name='supervisor')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    city = models.ForeignKey('smt_app.City', on_delete=models.CASCADE, null=True)
    zone = models.OneToOneField('smt_app.Zone', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class AssistanceSupervisor(models.Model):
    user = models.OneToOneField('smt_app.User', on_delete=models.CASCADE, null=True, related_name='ass_supervisor')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    city = models.ForeignKey('smt_app.City', on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey('smt_app.Zone', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class ShopOwner(models.Model):
    user = models.OneToOneField('smt_app.User', on_delete=models.CASCADE, null=True, related_name='shop_owner')
    shop_name = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    dob = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.id)


class Cleaner(models.Model):
    user = models.OneToOneField('smt_app.User', on_delete=models.CASCADE, null=True, related_name='cleaner')
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    city = models.ForeignKey('smt_app.City', on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey('smt_app.Zone', on_delete=models.CASCADE, null=True)
    cleaner_group = models.ForeignKey('shop_app.CleanerGroup', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)