from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.dates import MonthArchiveView

from django.shortcuts import get_object_or_404

from blogs import models

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.feedgenerator import Rss201rev2Feed


class BlogMixin:

    def get_queryset(self):
        """Filter jobs by current user."""
        return models.BlogPost.objects.filter(blog__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = get_object_or_404(models.Blog, slug=self.kwargs['slug'])
        context['blog'] = blog
        context['blogs'] = models.Blog.objects.all()
        dates = models.BlogPost.objects.filter(blog=blog).datetimes('created',
                                                                    'month')
        context['dates'] = dates
        tags = models.Tag.objects.filter(blog=blog)
        context['tags'] = tags
        categories = models.Category.objects.filter(blog=blog)
        context['categories'] = categories
        return context


class BlogPostListView(BlogMixin, ListView):

    template_name = 'blogs/list.html'


class BlogPostView(BlogMixin, DetailView):

    template_name = 'blogs/detail.html'
    slug_url_kwarg = 'post_slug'


class MonthArchiveView(BlogMixin, MonthArchiveView):
    template_name = 'blogs/list.html'
    date_field = 'created'
    allow_future = True
    month_format = '%m'
    make_object_list = True


class BlogPostTagView(BlogMixin, ListView):

    template_name = 'blogs/list.html'

    def get_queryset(self):
        """Filter jobs by current user."""
        queryset = super().get_queryset()
        return queryset.filter(tags__name=self.kwargs['tag_slug'])


class BlogPostCategoryView(BlogMixin, ListView):

    template_name = 'blogs/list.html'

    def get_queryset(self):
        """Filter jobs by current user."""
        queryset = super().get_queryset()
        return queryset.filter(categories__name=self.kwargs['category_slug'])


#########
# FEEDS #
#########


class BlogPostRSSFeed(Feed):
    feed_type = Rss201rev2Feed
    # general feed methods

    def get_object(self, request, slug):
        return get_object_or_404(models.Blog, slug=slug)

    def title(self, obj):
        return "Huseyin Yilmaz - {title}".format(title=obj.title)

    def description(self, obj):
        return obj.description

    def link(self, obj):
        return obj.get_absolute_url()

    # item methods
    def items(self, obj):
        return obj.blogpost_set.all().order_by('created')[:1000]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser_HTML

    def item_link(self, item):
        return item.get_absolute_url()


class BlogPostAtomFeed(BlogPostRSSFeed):
    feed_type = Atom1Feed
    subtitle = BlogPostRSSFeed.description
