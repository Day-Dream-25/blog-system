from django.urls import path

from user.api.views import UserCreate, UserListView, UserDestroyAPIView, UserUpdateAPIView, UserRetrieveAPIView

from user.views import UserLogin

urlpatterns = [

    path('createapi/', UserCreate.as_view()),
    path('userlogin/', UserLogin.as_view()),
    path('listapi/', UserListView.as_view()),
    path('destroyapi/<int:pk>', UserDestroyAPIView.as_view()),
    path('updateapi/<int:pk>', UserUpdateAPIView.as_view()),
    path('reteriveapi/<int:pk>', UserRetrieveAPIView.as_view()),
    path('createapi/', UserCreate.as_view()),

]