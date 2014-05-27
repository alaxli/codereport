#from django.shortcuts import render
from codereport.lib.django_util import render
from csreport.models import csproject,csreport
from csreport.tasks import get_data,get_codeline,get_problemline,get_trend,get_datelist
#from django.shortcuts import get_object_or_404
#from codereport.lib.exceptions_renderable import PopupException

import datetime
import simplejson as json
# Create your views here.

def data(request, searchstr = ''):
    datelist = get_datelist()
    if searchstr == '':
        date = datelist[0][0].strftime("%Y-%m-%d")
    else:
        date = searchstr

    dataset = get_data(date)
    return render("csreport/data.html",request,{
        'dataset': dataset,
        'datelist': datelist,
        'date': date,
        'request': request,
        })

def report(request):
    datelist = get_datelist()
    date = datelist[0][0].strftime("%Y-%m-%d")

    if request.method == 'POST':
        date = request.POST.get('dateselect');
    selectdate = date

    # cpp / java codeline
    cppcodeline = get_codeline('C/C++',date)
    javacodeline = get_codeline('Java',date)

    # cpp /java problem
    cppproblemline = get_problemline('C/C++',date)
    javaproblemline = get_problemline('Java',date)


    # cpp percent
    cpppercent = []
    length = len(cppproblemline)
    for i in range(length):
        cpppercent.append([])

    for i in range(length):
        cpppercent[i].append(cppproblemline[i][0])
        cpppercent[i].append(float("%.4f" % (1-cppproblemline[i][1]/cppcodeline[i][1])) * 100)

    # java percent
    javapercent = []
    length = len(javaproblemline)
    for i in range(length):
        javapercent.append([])

    for i in range(length):
        javapercent[i].append(javaproblemline[i][0])
        javapercent[i].append(float("%.4f" % (1-javaproblemline[i][1]/javacodeline[i][1])) * 100)

    cppcodeline = json.dumps(cppcodeline)
    javacodeline = json.dumps(javacodeline)
    cppproblemline = json.dumps(cppproblemline)
    javaproblemline = json.dumps(javaproblemline)
    cpppercent = json.dumps(cpppercent)
    javapercent = json.dumps(javapercent)

    #trend info
    resultset = get_trend()
    trendset = []
    for i in range(0,len(resultset)):
        trendset.append([])
        date = resultset[i][0].strftime("%Y-%m-%d")
        trendset[i].append(date)
        trendset[i].append(resultset[i][1])
        trendset[i].append(resultset[i][2])
    trendset = json.dumps(trendset)

    return render("csreport/report.html",request,{
        'datelist': datelist,
        'date': selectdate,
        'cppcodeline': cppcodeline,
        'javacodeline': javacodeline,
        'cppproblemline': cppproblemline,
        'javaproblemline': javaproblemline,
        'cpppercent': cpppercent,
        'javapercent': javapercent,
        'trendset' : trendset,
        'request': request,
        })

