from django.conf.urls import url
from django.views.decorators.cache import cache_page
from blogs import views

cache_fun = cache_page(10 * 60)

urlpatterns = [
    url('^(?P<slug>\S+)/rss/$',
        cache_fun(views.BlogPostRSSFeed()), name='blog-rss'),
    url('^(?P<slug>\S+)/atom/$',
        cache_fun(views.BlogPostAtomFeed()), name='blog-atom'),
    url('^(?P<slug>\S+)/category/(?P<category_slug>\S+)/$',
        views.BlogPostCategoryView.as_view(), name='blogs-category'),
    url('^(?P<slug>\S+)/tag/(?P<tag_slug>\S+)/$',
        views.BlogPostTagView.as_view(), name='blogs-tag'),
    url('^(?P<slug>\S+)/(?P<year>\d+)/(?P<month>\d+)/$',
        views.MonthArchiveView.as_view(), name='blogs-month'),
    url('^(?P<slug>\S+)/(?P<post_slug>\S+)/$',
        views.BlogPostView.as_view(), name='blogs-post'),
    url('^(?P<slug>\S+)/$',
        views.BlogPostListView.as_view(), name='blogs-list'),

]
