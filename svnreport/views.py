
#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from codereport.lib.django_util import render
from svnreport.models import svnproject,svnreport
from svnreport.tasks import get_svndata,get_svnreport,get_userreport
from svnreport.tasks import get_codeline,get_datelist,get_department
from svnreport.tasks import get_language,get_count
#from django.core.serializers.json import DjangoJSONEncoder
#from django.shortcuts import get_object_or_404
#from codereport.lib.exceptions_renderable import PopupException

import datetime
import re
import simplejson as json
# Create your views here.
searchstr_pattern = re.compile(r"^f(\d+-\d+-\d+)to(\d+-\d+-\d+)")


def data(request, searchstr = ''):
    if searchstr == '':
        today = datetime.date.today()
        end_date = today - datetime.timedelta(days=1)
        start_date = today - datetime.timedelta(days=8)
    else:
        result = searchstr_pattern.match(searchstr)
        start_date, end_date = result.groups(1)
        start_date=datetime.datetime.strptime(start_date,"%Y-%m-%d")
        end_date=datetime.datetime.strptime(end_date,"%Y-%m-%d")

    svndataset = get_svndata(start_date,end_date)
    return render("svnreport/data.html",request,{
        'svndataset': svndataset,
        'end_date' : end_date,
        'start_date' : start_date,
        'request': request,
        })

def updatereport(request):
    today = datetime.date.today()
    end_date = today - datetime.timedelta(days=1)
    start_date = today - datetime.timedelta(days=8)
    
    if request.method == 'POST':
        searchstr = request.POST.get('start_date')
        if searchstr == '':
            start_date = start_date
            #return HttpResponseRedirect(urlresolvers.reverse('updatereport'))
        else:
            start_date = datetime.datetime.strptime(searchstr,"%Y-%m-%d")
        searchstr = request.POST.get('end_date')
        if searchstr == '':
            end_date = end_date
            #return HttpResponseRedirect(urlresolvers.reverse('updatereport'))
        else:
            end_date = datetime.datetime.strptime(searchstr,"%Y-%m-%d")

    svnuserset = get_userreport(start_date,end_date)
    resultset = get_svnreport(start_date,end_date)

    svnprojects = svnproject.objects.all()
    svnreportdict = {}
    for project in svnprojects:
        if not project.department in svnreportdict:
            svnreportdict[project.department] = {}
    for project in svnprojects:
        svnreportdict[project.department][project.groups] = 0

    for row in resultset:
        svnreportdict[row[0]][row[1]]=int(row[2])
    svnreportset = json.dumps(svnreportdict)

    return render("svnreport/updatereport.html",request,{
        'svnuserset': svnuserset,
        'svnreportdict': svnreportdict,
        'svnreportset': svnreportset,
        'end_date' : end_date,
        'start_date' : start_date,
        'request': request,
        })

def codeline(request):
    resultset = get_codeline()
    codelineset = []
    for i in range(0,len(resultset)):
        codelineset.append([])
        date = resultset[i][0].strftime("%Y-%m-%d")
        codelineset[i].append(date)
        codelineset[i].append(resultset[i][1])
        codelineset[i].append(resultset[i][2])

    codelineset = json.dumps(codelineset)

    datelist = get_datelist()
    date = datelist[0][0].strftime("%Y-%m-%d")

    departmentdict = {}
    departmentset= get_department(date)
    for row in departmentset:
        (department,language,count) = row
        if not departmentdict.has_key(department):
            departmentdict[department] = {}
        departmentdict[department][language]=count
    departmentset = json.dumps(departmentdict)

    #languagedict = {}
    languageset= get_language(date)
    #for row in languageset:
    #    (language,department,count) = row
    #    if not languagedict.has_key(language):
    #        languagedict[language] = {}
    #    languagedict[language][department]=count
    languageset = json.dumps(languageset)
    date = json.dumps(date)

    count_department = get_count('department','svnreport_svnproject')
    count_groups = get_count('groups','svnreport_svnproject')
    count_users = get_count('svnuser','svnreport_svnreport')
    count_language = get_count('language','svnreport_codeline')
    return render("svnreport/codeline.html",request,{
        'codelineset': codelineset,
        'departmentset': departmentset,
        'languageset': languageset,
        'date': date,
        'count_department': count_department,
        'count_groups': count_groups,
        'count_users': count_users,
        'count_language': count_language,
        'request': request,
        })

