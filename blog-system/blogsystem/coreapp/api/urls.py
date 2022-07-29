from django.urls import path

from coreapp.api.views import ProfileCreateAPIView, \
    ProfileDestroyAPIView, ProfileUpdateAPIView, ProfileRetrieveAPIView


urlpatterns = [


    path('createapi/', ProfileCreateAPIView.as_view()),
    path('destroyapi/<int:pk>', ProfileDestroyAPIView.as_view()),
    path('updateapi/<int:pk>', ProfileUpdateAPIView.as_view()),
    path('retriveapi/<int:pk>', ProfileRetrieveAPIView.as_view()),

]
