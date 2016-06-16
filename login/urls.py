#coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from login_user.views import login,login_auth
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'^login_auth/',login_auth)

)
