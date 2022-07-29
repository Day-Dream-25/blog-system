from django.urls import path

from user_app.views import ManagerView, SupervisorCreateView, AssSupervisorView, ManagerListView, \
    SupervisorListView, AssSupervisorListView, ManagerUpdateView, SupervisorUpdateView, AssSupervisorUpdateView, \
    ManagerDetailView, SupervisorDetailView, AssSupervisorDetailView, SupervisorDeleteView, AssSupervisorDeleteView, \
    CleanerView, CleanerDeleteView, CleanerUpdateView, CleanerDetailView, CleanerListView, Shop_OwnerListView, \
    Shop_OwnerUpdateView, Shop_OwnerDeleteView, Shop_OwnerDetailView, Shop_OwnerView

urlpatterns = [
    path('manager/', ManagerView.as_view(), name="manager"),
    path('supervisor/', SupervisorCreateView.as_view(), name="supervisor"),
    path('asssupervisor/', AssSupervisorView.as_view(), name="asupervisor"),
    path('cleaner/', CleanerView.as_view(), name="cleaner"),
    # path('shopmanager/', Shop_ManagerView.as_view(), name="shopmanager"),
    path('shopowner/', Shop_OwnerView.as_view(), name="shopowner"),

    path('managerlist/<int:pk>/', ManagerListView.as_view(), name='managerlist'),
    path('supervisorlist/<int:pk>', SupervisorListView.as_view(), name='supervisorlist'),
    path('asupervisorlist/<int:pk>', AssSupervisorListView.as_view(), name='asupervisorlist'),
    path('cleanerlist/<int:pk>/', CleanerListView.as_view(), name='cleanerlist'),
    # path('shopmanagerlist/<int:pk>/', Shop_ManagerListView.as_view(), name='shopmanagerlist'),
    path('shopownerlist/', Shop_OwnerListView.as_view(), name='shopownerlist'),

    path('updatemanager/<int:pk>/', ManagerUpdateView.as_view(), name="updatemanager"),
    path('updatesupervisor/<int:pk>/', SupervisorUpdateView.as_view(), name='updatesupervisor'),
    path('updateasupervisor/<int:pk>/', AssSupervisorUpdateView.as_view(), name='updateasupervisor'),
    path('updatecleaner/<int:pk>/', CleanerUpdateView.as_view(), name="updatecleaner"),
    # path('updateshopmanager/<int:pk>/', Shop_ManagerUpdateView.as_view(), name='updateshopmanager'),
    path('updateshopowner/<int:pk>/', Shop_OwnerUpdateView.as_view(), name='updateshopowner'),

    path('deletesupervisor/<int:pk>/', SupervisorDeleteView.as_view(), name='deletesupervisor'),
    path('deleteasupervisor/<int:pk>/', AssSupervisorDeleteView.as_view(), name='deleteasupervisor'),
    path('deletecleaner/<int:pk>/', CleanerDeleteView.as_view(), name='deletecleaner'),
    # path('deleteshopmanager/<int:pk>/', Shop_ManagerDeleteView.as_view(), name='deleteshopmanager'),
    path('deleteshopowner/<int:pk>/', Shop_OwnerDeleteView.as_view(), name='deleteshopowner'),

    path('detailmanager/<int:pk>/', ManagerDetailView.as_view(), name='detailmanager'),
    path('detailsupervisor/<int:pk>/', SupervisorDetailView.as_view(), name='detailsupervisor'),
    path('detailasupervisor/<int:pk>/', AssSupervisorDetailView.as_view(), name='detailasupervisor'),
    path('detailcleaner/<int:pk>/', CleanerDetailView.as_view(), name='detailcleaner'),
    # path('detailshopmanager/<int:pk>/', Shop_ManagerDetailView.as_view(), name='detailshopmanager'),
    path('detailashopowner/<int:pk>/', Shop_OwnerDetailView.as_view(), name='detailashopowner'),


]