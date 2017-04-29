from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.index, name='core-index'),
    url(r'^sp/aboutme/$', views.about, name='core-about'),
]
