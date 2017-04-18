from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.dates import MonthArchiveView

from django.shortcuts import get_object_or_404

from blogs import models


class BlogMixin:

    def get_queryset(self):
        """Filter jobs by current user."""
        return models.BlogPost.objects.filter(blog__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = get_object_or_404(models.Blog, slug=self.kwargs['slug'])
        context['blog'] = blog
        dates = models.BlogPost.objects.filter(blog=blog).datetimes('created', 'month')
        context['dates'] = dates
        return context


class BlogPostListView(BlogMixin, ListView):

    template_name = 'blogs/list.html'


class BlogPostView(BlogMixin, DetailView):

    template_name = 'blogs/detail.html'
    slug_url_kwarg = 'post_slug'
