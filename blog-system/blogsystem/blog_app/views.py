from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from blog_app.forms import BlogForm
from blog_app.models import Blog


class BlogCreateView(CreateView):
    template_name = 'blog/add_blog.html'
    model = Blog
    form_class = BlogForm
    success_url = "/bloglist/"

    def get_success_url(self):
        return reverse('blogs_list')


class BlogsListView(ListView):
    template_name = 'home.html'
    model = Blog

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        if self.request.GET.get('current_user'):
            return qs.filter(user_id=self.request.user.id)
        return qs


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Blog
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'post_id'
    query_pk_and_slug = False

