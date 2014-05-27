from django.db import models

# Create your models here.


class csproject(models.Model):
    '''
    coding standard project info
    '''
    name = models.CharField(max_length = 50, blank = False)
    language = models.CharField(max_length = 20, blank = False)
    svnpath = models.CharField(max_length = 100, null = True, blank = True)
    groups = models.CharField(max_length = 20, null = True, blank = True)
    department = models.CharField(max_length = 20, null = True, blank = True)

    def __unicode__(self):
        return u'%s' % (self.name)

class csreport(models.Model):
    '''
    the report data from sonarqube
    '''
    project = models.ForeignKey('csproject', related_name = 'cs_report', null = True, on_delete = models.SET_NULL)
    codeline = models.IntegerField()
    commentline = models.IntegerField()
    duplicateline = models.IntegerField()
    problemline = models.IntegerField()
    date = models.DateTimeField(null = False)

    def __unicode__(self):
        return u'%s' %(self.id)
