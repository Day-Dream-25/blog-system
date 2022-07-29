from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, related_name='blog_user')
    title = models.CharField(max_length=25)
    image = models.ImageField(blank=True, upload_to='images/')
    Date = models.DateField(default=datetime.now().date())
    description = models.CharField(max_length=1000)
    Update_date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

