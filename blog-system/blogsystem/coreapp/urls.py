from django.urls import path

from coreapp.views import ProfileCreateView, ProfileUpdate1View, contact

urlpatterns = [
    path('profile_create', ProfileCreateView.as_view(), name="profile_create"),
    path('profile_update/<int:pk>/', ProfileUpdate1View.as_view(), name="profile_update"),
    path("contact", contact, name="contact"),
]