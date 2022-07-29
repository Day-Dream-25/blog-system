from django.urls import path

from blog_app.views import BlogCreateView, BlogDetailView,BlogsListView

urlpatterns = [


    path('blog_craete/', BlogCreateView.as_view(), name="blog_craete"),
    path('blogslist/', BlogsListView.as_view(), name="blogs_list"),
    path('blogdetail/<slug:slug>/', BlogDetailView.as_view(), name="blogdetail"),

]
