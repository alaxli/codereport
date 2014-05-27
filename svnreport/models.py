from django.db import models

# Create your models here.


class svnproject(models.Model):
    '''
    svn project info
    '''
    name = models.CharField(max_length = 20, blank = False)
    svnpath = models.CharField(max_length = 100, null = True, blank = True)
    groups = models.CharField(max_length = 20, null = True, blank = True)
    department = models.CharField(max_length = 20, null = True, blank = True)
    lastrev = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.name)

class svnreport(models.Model):
    '''
    the report data from svn
    '''
    svnproject = models.ForeignKey('svnproject', related_name = 'svn_report', null = True, on_delete = models.SET_NULL)
    svnuser = models.CharField(max_length = 20, null = False)
    svndate = models.DateTimeField(null = False)
    svncommit = models.IntegerField()
    svnadd = models.IntegerField()
    svndelete = models.IntegerField()

    def __unicode__(self):
        return u'%s' %(self.id)

class codeline(models.Model):
    '''
    the report of codeline from svn
    '''
    svnproject = models.ForeignKey('svnproject', related_name = 'codeline', null = True, on_delete = models.SET_NULL)
    language = models.CharField(max_length = 20, null = False)
    files = models.IntegerField()
    code = models.IntegerField()
    comment = models.IntegerField()
    commentpercent = models.DecimalField(max_digits=4, decimal_places=2)
    blank = models.IntegerField()
    date = models.DateField(null = False)

    def __unicode__(self):
        return u'%s' %(self.id)
