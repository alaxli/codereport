from django.contrib import admin

# Register your models here.
from svnreport.models import svnproject,svnreport,codeline

class svnprojectAdmin(admin.ModelAdmin):
    '''
    docstring for svnprojectAdmin
    '''
    list_display = ('name', 'svnpath', 'groups', 'department', 'lastrev')

class svnreportAdmin(admin.ModelAdmin):
    '''
    docstring for svnreportAdmin
    '''
    list_display = ('svnproject', 'svnuser', 'svndate', 'svncommit', 'svnadd', 'svndelete')
    search_fields = ['svnuser']

class codelineAdmin(admin.ModelAdmin):
    '''
    docstring for codelineAdmin
    '''
    list_display = ('svnproject', 'language', 'files', 'code', 'comment', 'commentpercent','blank','date')
    search_fields = ['date']

admin.site.register(svnproject, svnprojectAdmin)
admin.site.register(svnreport, svnreportAdmin)
admin.site.register(codeline, codelineAdmin)
