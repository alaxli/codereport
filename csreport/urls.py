from django.conf.urls import patterns, url
from codereport.lib.django_util import get_name_re_rule,get_id_re_rule

name_re = get_name_re_rule()
id_re=get_id_re_rule()

urlpatterns = patterns('csreport.views',
    url(r'^$', 'report', name = 'report'),
    url(r'^report$', 'report', name = 'report'),
    url(r'^data$', 'data', name = 'data'),
    url(r'^data/(?P<searchstr>%s)$' % name_re ,'data',name='data'),
)
