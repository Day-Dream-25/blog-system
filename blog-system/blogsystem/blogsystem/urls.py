"""blogsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('core/', include("coreapp.urls")),
    path('blog/', include("blog_app.urls")),
    path('user/', include("user.urls")),
    path('blog-api/', include("blog_app.api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('core-api/', include("coreapp.api.urls")),
    path('user-api/', include("user.api.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
