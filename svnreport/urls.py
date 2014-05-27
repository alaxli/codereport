from django.conf.urls import patterns, url
from codereport.lib.django_util import get_name_re_rule,get_id_re_rule

name_re = get_name_re_rule()
id_re=get_id_re_rule()

urlpatterns = patterns('svnreport.views',
    url(r'^$', 'updatereport', name = 'updatereport'),
    url(r'^data$', 'data', name = 'data'),
    url(r'^updatereport$', 'updatereport', name = 'updatereport'),
    url(r'^data/(?P<searchstr>%s)$' % name_re ,'data',name='data'),
    url(r'^codeline$', 'codeline', name = 'codeline'),
)
