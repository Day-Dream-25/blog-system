from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from shop_app.models import Shop
from user_app.models import Manager, Supervisor, AssistanceSupervisor, Cleaner, ShopOwner


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
            # "SHOP": shop_detail.objects.all(),
            "SHOP OWNER": ShopOwner.objects.all()
        }
        # return data.get(self.roll.filter(user_id=self.id).first()
        return data.get(self.roll).filter(user_id=self.id).first()


class City(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return str(self.city)


class Zone(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    zone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.zone)





