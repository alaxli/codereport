from django.contrib import admin

# Register your models here.
from csreport.models import csproject,csreport

class csprojectAdmin(admin.ModelAdmin):
    '''
    docstring for csprojectAdmin
    '''
    list_display = ('name', 'language', 'svnpath', 'groups', 'department')

class csreportAdmin(admin.ModelAdmin):
    '''
    docstring for csreportAdmin
    '''
    list_display = ('project', 'codeline', 'commentline', 'duplicateline', 'problemline', 'date')
    search_fields = ['project']

admin.site.register(csproject, csprojectAdmin)
admin.site.register(csreport, csreportAdmin)
