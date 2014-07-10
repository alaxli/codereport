About
=====
该系统为代码统计、代码规范等信息提供报表。

代码统计数据来源于[ohcount](https://github.com/blackducksw/ohcount)

代码规范数据来源于[sonarqube](http://www.sonarqube.org)

动态图表大多基于[Highcharts.js](http://www.hcharts.cn)。


Function
=====
* 提供部门、项目组、开发人员、语言种类数量统计 
* 提供代码库中各部门代码数量统计、各语言代码数量统计
* 提供各部门代码数量增长趋势
* 提供每周各部门、各项目组的代码更新量
* 提供每周个人代码更新量排行榜
* 提供每周代码规范统计(C++/Java)
* 提供代码规范发展趋势


Requirements
=====
* pip
* virtualenv
* mysql-devel
* openldap-devel

Install
=====
* 配置virtualenv环境


        virtualenv yourenv
        source yourenv/bin/activate


* 安装依赖库


        cd codereport
        pip install -r requirements.txt


* 配置ldap和数据库信息


        cd codereport
        mv settings.example internal
        cd internal
        mv settings_local.py.example settings_local.py
        vim settings_local.py #配置LDAP信息和数据库信息
        如果暂时不用ldap，需要修改settings.py,注释掉下面一行
        #    'codereport.auth.backend.LdapBackend',


* 配置数据库


        create database codereport CHARACTER SET utf8;
        grant all on codereport.* to codeuser@'localhost' identified by '*****';


* 初始化数据库


        python manage.py syncdb
        python manage.py schemamigration svnreport --init
        python manage.py schemamigration csreport --init 
        python manage.py migrate svnreport
        python manage.py migrate csreport


Run
=====
* 直接运行


        python manage.py runserver ip:8000


* Apache + wsgi :将apache-conf下 codereport.conf 文件拷贝至apache配置目录下，重启httpd


Demo
=====
* http://115.28.87.99:8080 用户名:root 密码:codereport

