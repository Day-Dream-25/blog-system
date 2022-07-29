from django.contrib import admin

# Register your models here.
from blog_app.models import Blog


# admin.site.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)
