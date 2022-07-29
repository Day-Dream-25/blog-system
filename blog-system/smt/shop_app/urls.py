from django.urls import path

from shop_app.views import ShopView, ShopDetailCreateView, ShopDetailListView, ShopListView \
    , ShopUpdateView, ShopDetailUpdateView, ShopDeleteView, ShopDetailDeleteView, ShopDetailView, ShopDetailsView, \
    CleanerGroupView, ShopWorkerView, CleanerGroupListView, ShopWorkerListView, CleanerGroupUpdateView, \
    ShopWorkerUpdateView, CleanerGroupDeleteView, ShopWorkerDeleteView, CleanerGroupDetailView, ShopWorkerDetailView, \
    AttendenceCreateView, AttendenceListView, historyListView, CleaningResult, AssignCleanerView, AssignCleanerListView, \
    AssignCleanersupervisorListView,\
    AssignCleanerSownerView, AssignCleanerAssupervisorView, AssignCleanersupervisorView

urlpatterns = [
    path('shop/', ShopView.as_view(), name="shop"),
    path('shopdetail/', ShopDetailCreateView.as_view(), name="shopdetail"),
    path('cleanergroup/', CleanerGroupView.as_view(), name="cleanergroup"),
    path('shopworker/', ShopWorkerView.as_view(), name="shopworker"),
    path('attendence/<int:pk>', AttendenceCreateView.as_view(), name="attendence"),
    path('assigncleaner/', AssignCleanerView.as_view(), name="assigncleaner"),

    path('acsupervisor/<int:pk>', AssignCleanersupervisorView.as_view(), name="acsupervisor"),
    path('acasupervisor/<int:pk>', AssignCleanerAssupervisorView.as_view(), name="acasupervisor"),
    path('acowner/<int:pk>', AssignCleanerSownerView.as_view(), name="acowner"),

    path('shoplist/<int:pk>/', ShopListView.as_view(), name='sahoplist'),
    path('shopdetaillist/<int:pk>', ShopDetailListView.as_view(), name='shopdetaillist'),
    path('cleanergrouplist/<int:pk>', CleanerGroupListView.as_view(), name="cleanergrouplist"),
    path('shopworkerlist/<int:pk>', ShopWorkerListView.as_view(), name="shopworkerlist"),
    path('attenddencelist/<int:pk>', AttendenceListView.as_view(), name="attenddencelist"),
    path('historylist/<int:pk>', historyListView.as_view(), name="historylist"),
    path('assigncleanerlist/', AssignCleanerListView.as_view(), name="assigncleanerlist"),

    path('acsupervisoelist/', AssignCleanersupervisorListView.as_view(), name="acsupervisoelist"),
    # path('acasupervisorlist/', AssignCleanerAssupervisorListView.as_view(), name="acasupervisorlist"),
    # path('acowner/', AssignCleanersownerListView.as_view(), name="acowner"),


    path('shopupdate/<int:pk>/', ShopUpdateView.as_view(), name='shopupdate'),
    path('shopdetailupdate/<int:pk>', ShopDetailUpdateView.as_view(), name='shopdetailupdate'),
    path('cleanergroupupdate/<int:pk>', CleanerGroupUpdateView.as_view(), name="cleanergroupupdate"),
    path('shopworkerupdate/<int:pk>', ShopWorkerUpdateView.as_view(), name="shopworkerupdate"),

    path('shopdelete/<int:pk>/', ShopDeleteView.as_view(), name='shopdelete'),
    path('shopdetaildelete/<int:pk>', ShopDetailDeleteView.as_view(), name='shopdetaildelete'),
    path('cleanergroupdelete/<int:pk>', CleanerGroupDeleteView.as_view(), name="cleanergroupdelete"),
    path('shopworkerdelete/<int:pk>', ShopWorkerDeleteView.as_view(), name="shopworkerdelete"),

    path('shoplist/<int:pk>/', ShopDetailView.as_view(), name='shoplist'),
    path('shopdetaildetails/<int:pk>', ShopDetailsView.as_view(), name='shopdetaildetails'),
    path('cleannergroupdetail/<int:pk>', CleanerGroupDetailView.as_view(), name="cleannergroupdetail"),
    path('shopworkerdetails/<int:pk>', ShopWorkerDetailView.as_view(), name="shopworkerdetails"),

    path('cleanningrecord/', CleaningResult.as_view(), name="cleanningrecord"),

]