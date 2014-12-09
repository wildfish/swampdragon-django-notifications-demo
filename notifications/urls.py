from django.conf.urls import patterns, include, url
from django.contrib import admin
from demo.views import Notifications

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Notifications.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
