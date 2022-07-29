
from django.urls import path

from user import views
from user.views import UserRegistration, UserUpdateView, Logout, UserLogin


urlpatterns = [
    path('', UserRegistration.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name="login"),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='updateuser'),
    path('logout/', Logout.as_view(), name="logout"),

]
