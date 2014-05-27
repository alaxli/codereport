from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

import svnreport.urls
import csreport.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codereport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    (r'^accounts/login/$', 'codereport.auth.views.dt_login'),
    (r'^accounts/logout/$', 'codereport.auth.views.dt_logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^svnreport/', include(svnreport.urls)),
    url(r'^csreport/', include(csreport.urls)),

)
