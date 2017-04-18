from django.conf.urls import url

from blogs import views

urlpatterns = [
    url('^(?P<slug>\S+)/(?P<post_slug>\S+)/$',
        views.BlogPostView.as_view(), name='blogs-post'),
    url('^(?P<slug>\S+)/$',
        views.BlogPostListView.as_view(), name='blogs-list'),
]
