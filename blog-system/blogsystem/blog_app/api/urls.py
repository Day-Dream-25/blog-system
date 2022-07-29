from django.urls import path
from rest_framework.routers import DefaultRouter

from blog_app.api.views import BlogViewSet, BlogCreate, BlogListView, BlogDestroyAPIView, BlogUpdateAPIView,\
     BlogRetrieveAPIView

router = DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [

    path('createapi/', BlogCreate.as_view()),
    path('listapi/', BlogListView.as_view()),
    path('destroyapi/<int:pk>', BlogDestroyAPIView.as_view()),
    path('updateapi/<int:pk>', BlogUpdateAPIView.as_view()),
    path('reteriveapi/<int:pk>', BlogRetrieveAPIView.as_view()),

]
urlpatterns += router.urls
