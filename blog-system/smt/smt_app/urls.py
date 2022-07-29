from django.urls import path

from smt_app.views import UserRegistration, UserLogin, UserUpdateView, Logout

urlpatterns = [
    path('', UserRegistration.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name="login"),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='updateuser'),
    path('logout/', Logout.as_view(), name="logout"),

  ]