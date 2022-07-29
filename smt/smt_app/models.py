from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    Roll_Choices = (
        ("MANAGER", "MANAGER"),
        ("SUPERVISOR", "SUPERVISOR"),
        ("ASSISTANT SUPERVISOR", "ASSISTANT SUPERVISOR"),
        ("CLEANER", "CLEANER"),
        # ("SHOP", "SHOP"),
        ("SHOP OWNER", "SHOP OWNER")

    )

    phone_no = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50, blank=True)
    roll = models.CharField(
        max_length=20,
        choices=Roll_Choices, default="MANAGER"
    )

    def __str__(self):
        return str(self.username)

    @property
    def category_id(self):
        # import pdb; pdb.set_trace()
        data = {
            "MANAGER": Manager.objects.all(),
            "SUPERVISOR": Supervisor.objects.all(),
            "ASSISTANT SUPERVISOR": AssistanceSupervisor.objects.all(),
            "CLEANER": Cleaner.objects.all(),
            # "SHOP": Shop_Detail.objects.all(),
            "SHOP OWNER": Shop.objects.all()
        }
        # return data.get(self.roll.filter(user_id=self.id).first()
        return data.get(self.roll).filter(user_id=self.id).first()


class City(models.Model):
    city = models.CharField(max_length=30)


class Zone(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.CharField(max_length=20)


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='manager')
    name = models.CharField(max_length=10)
    city = models.OneToOneField(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='supervisor')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.OneToOneField(Zone, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class AssistanceSupervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='ass_supervisor')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


class Tax(models.Model):
    shop_category = models.CharField(max_length=20)
    amount = models.IntegerField(null=True)


class CleanerGroup(models.Model):
    group_name = models.CharField(max_length=20)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null= True, related_name='cleaner_group_supervisor')


class Cleaner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='cleaner')
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True)
    cleaner_group = models.ForeignKey(CleanerGroup, on_delete=models.SET_NULL, null=True )
    # working_hours = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='shopdetail')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True)
    electricity_meter = models.IntegerField()
    shop_no = models.IntegerField()
    history = models.ManyToManyField("smt_app.Shop_Detail",  related_name='history_shop')

    def __str__(self):
        return str(self.id)


class ShopDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='shop')
    ass_supervisor = models.ForeignKey(AssistanceSupervisor, on_delete=models.CASCADE, null=True)
    shop_detail = models.OneToOneField(Shop, on_delete=models.CASCADE, null=True )
    shop_owner = models.ManyToManyField("smt_app.Shop_Owner", related_name='shopowner_shopdetail')
    age = models.IntegerField(null=True)
    category = models.ForeignKey(Tax, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.id)


class ShopOwner(models.Model):
    shop_name = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    dob = models.CharField(max_length=30, null=True)


class CleanerRecord(models.Model):
    date = models.DateField()
    records = models.BooleanField()
    group = models.ForeignKey(Cleaner, on_delete=models.CASCADE, null=True)
    shop_detail = models.OneToOneField(ShopDetail, on_delete=models.CASCADE, null=True)


class ShopWorker(models.Model):
    shop_detail = models.ForeignKey(ShopDetail, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
