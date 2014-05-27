# coding=utf-8
import MySQLdb
from codereport.internal import settings_local

def get_data(date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select name,language,codeline,problemline,groups,department,date \
                from csreport_csproject,csreport_csreport \
                where date='%s' \
                and csreport_csproject.id=csreport_csreport.project_id;" % date
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_codeline(language,date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select groups,sum(codeline) \
                from csreport_csproject,csreport_csreport \
                where date='%s' \
                and csreport_csproject.id=csreport_csreport.project_id \
                and language='%s' \
                group by groups;" % (date,language)
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_problemline(language,date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select groups,sum(problemline) \
                from csreport_csproject,csreport_csreport \
                where date='%s' \
                and csreport_csproject.id=csreport_csreport.project_id \
                and language='%s' \
                group by groups;" % (date,language)
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset


def get_trend():
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select date,language,(1-sum(problemline)/sum(codeline))*100 \
                from csreport_csproject,csreport_csreport \
                where language!='python' \
                and csreport_csproject.id=csreport_csreport.project_id \
                group by date,language;"
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset


def get_datelist():
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select date from csreport_csreport group by date order by date DESC;"
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset
