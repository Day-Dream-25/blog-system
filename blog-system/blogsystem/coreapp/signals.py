from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from coreapp.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('created')
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # import pdb; pdb.set_trace()
    instance.profile_user.save()
