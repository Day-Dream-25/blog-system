from django.db import models


class Profile(models.Model):
    TYPE_SELECT = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='profile_user')
    gender = models.CharField(max_length=11, choices=TYPE_SELECT)
    dob = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)
    link = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self, ** kwargs):
        super().save()


class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact_no = models.CharField(max_length=12)
    message = models.CharField(max_length=100)
