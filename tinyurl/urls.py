from django.conf.urls import patterns, include, url

from django.contrib import admin
from tinyurl.index.views import IndexView, UrlDetail, UrlRedirect, UrlList

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/(?P<slug>\w+)/$', UrlDetail.as_view(), name='detail'),
    url(r'^list/$', UrlList.as_view(), name='list'),
    url(r'^url_api/$', 'tinyurl.index.views.url_api', name='url_api'),
    url(r'^(?P<slug>\w+)/$', UrlRedirect.as_view(), name='redirect'),
    url(r'^admin/', include(admin.site.urls)),
)
