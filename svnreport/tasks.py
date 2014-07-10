# coding=utf-8
import MySQLdb
from codereport.internal import settings_local

def get_svndata(start_date,end_date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select department,groups,svnuser,svndate,svncommit,svnadd \
                from svnreport_svnproject,svnreport_svnreport \
                where date(svndate) >= '%s' and date(svndate) <= '%s' \
                and svnreport_svnproject.id=svnreport_svnreport.svnproject_id \
                order by svndate DESC;" % (start_date,end_date)
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_svnreport(start_date,end_date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select department,groups,sum(svnadd) \
                from svnreport_svnproject,svnreport_svnreport \
                where date(svndate) >= '%s' and date(svndate) <= '%s' \
                and svnreport_svnproject.id=svnreport_svnreport.svnproject_id \
                group by department,groups;" % (start_date,end_date)
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_userreport(start_date,end_date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select department,groups,svnuser,sum(svnadd) \
                from svnreport_svnproject,svnreport_svnreport \
                where date(svndate) >= '%s' and date(svndate) <= '%s' \
                and svnreport_svnproject.id=svnreport_svnreport.svnproject_id \
                group by svnuser order by sum(svnadd) DESC;" % (start_date,end_date)
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_codeline():
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select date,department,sum(code) \
                from svnreport_svnproject,svnreport_codeline \
                where svnreport_codeline.language='Total' \
                and svnreport_svnproject.id=svnreport_codeline.svnproject_id \
                group by date,department order by date;"
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
        command = "select date from svnreport_codeline group by date order by date DESC;"
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset


def get_department(date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select department,language,sum(code) \
                from svnreport_svnproject,svnreport_codeline \
                where svnreport_codeline.language != 'Total' \
                and svnreport_codeline.date = '%s' \
                and svnreport_svnproject.id=svnreport_codeline.svnproject_id \
                group by department,language;" % date
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_language(date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select language,sum(code) \
                from svnreport_svnproject,svnreport_codeline \
                where svnreport_codeline.language != 'Total' \
                and svnreport_codeline.date = '%s' \
                and svnreport_svnproject.id=svnreport_codeline.svnproject_id \
                group by language order by sum(code) DESC;" % date
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset

def get_count(item,table):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select %s from %s group by %s;" % (item,table,item)
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return len(resultset)

def get_department_groups(date):
    resultset = []
    try:
        conn = MySQLdb.connect(host = settings_local.DATABASES['default']['HOST'],
                user = settings_local.DATABASES['default']['USER'],
                passwd = settings_local.DATABASES['default']['PASSWORD'],
                db = settings_local.DATABASES['default']['NAME'],
                port = int(settings_local.DATABASES['default']['PORT']),
                charset='utf8')
        cur = conn.cursor()
        command = "select department,groups,sum(code) \
                from svnreport_svnproject,svnreport_codeline \
                where svnreport_codeline.language = 'Total' \
                and svnreport_codeline.date = '%s' \
                and svnreport_svnproject.id=svnreport_codeline.svnproject_id \
                group by department,groups;" % date
        cur.execute(command)
        for row in cur.fetchall():
            resultset.append(row)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return resultset
