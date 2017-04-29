from django.conf.urls import url
from django.views.decorators.cache import cache_page
from blogs import views

# TODO move this to a cache mixin.
cache_fun = cache_page(10 * 60)

urlpatterns = [
    url('^(?P<slug>\S+)/rss/$',
        cache_fun(views.BlogPostRSSFeed()), name='blog-rss'),
    url('^(?P<slug>\S+)/atom/$',
        cache_fun(views.BlogPostAtomFeed()), name='blog-atom'),
    url('^(?P<slug>\S+)/category/(?P<category_slug>\S+)/$',
        cache_fun(views.BlogPostCategoryView.as_view()), name='blogs-category'), # noqa
    url('^(?P<slug>\S+)/tag/(?P<tag_slug>\S+)/$',
        cache_fun(views.BlogPostTagView.as_view()), name='blogs-tag'),
    url('^(?P<slug>\S+)/(?P<year>\d+)/(?P<month>\d+)/$',
        cache_fun(views.MonthArchiveView.as_view()), name='blogs-month'),
    url('^(?P<slug>\S+)/(?P<post_slug>\S+)/$',
        cache_fun(views.BlogPostView.as_view()), name='blogs-post'),
    url('^(?P<slug>\S+)/$',
        cache_fun(views.BlogPostListView.as_view()), name='blogs-list'),

]
