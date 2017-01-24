#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/20 15:52
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : app.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.gen
import os
import tornado.httpserver
import MySQLdb
import torndb
import fetchcatalog
from concurrent.futures import ThreadPoolExecutor
'''
db = MySQLdb.connect('localhost','root','123456','blog', charset="utf8")
cursor = db.cursor()
sql = """select * from blog;"""
cursor.execute(sql)
results = cursor.fetchall()
#print results
catalog = fetchcatalog.htmlparser(results[0][3])
c = {}
for i in results:
    c[i[0]] = (i[1],i[2])
print c
'''

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="dang database host")
define("mysql_database", default="blog", help="dang database name")
define("mysql_user", default="root", help="dang database user")
define("mysql_password", default="123456", help="dang database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/?', HomeHandler),
            (r'/archives/?(.*)', ArchivesHandler),
            (r'/about/?', AboutHandler),
            (r'/submit/?', SubmitHandler),
            (r'/p/?(.*)',EssayHandler),
            (r'/category/?(.*)', CategoryHandler),
            (r'/date/?(.*)', DateHandler),
            (r'/admin/?(.*)', AdminHandler),
            (r'/del/?(.*)', DelHandler),
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            #xsrf_cookies=True,
            #cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            #login_url="/login",
            #debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password,charset="utf8")


class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(2)
    @property       # 将db方法变为属性
    def db(self):
        return self.application.db

    def query(self, sql):
        sen = self.db.query(sql)
        return sen

    def exesql(self, sql):
        self.db.execute(sql)

    def get_current_user(self):
        '''
        user_id = self.get_secure_cookie("username")
        if not user_id:
            return None
        return user_id
        '''
        pass

class HomeHandler(BaseHandler):
    def get(self):
        self.render('home.html')

class ArchivesHandler(BaseHandler):
    def get(self, page=''):
        sql = 'SELECT count(*) FROM blog;'
        sql1 = 'select identity, count(*) from blog group by identity;'
        sql2 = 'SELECT date, count(*) FROM blog group by date;'

        results = self.query(sql)

        lastPage=1      # 上一页
        currentPage=1       # 当前页面
        nextPage=1      # 下一页
        perPage = 8     # 每页多少行
        totalItem = int(results[0].values()[0]) # 总共有几条
        totalPage = totalItem/perPage if totalItem % perPage == 0 else totalItem/perPage + 1    # 总共分几页面
        identies = self.query(sql1)     # 查看分类及分类对应总数
        date = self.query(sql2)     # 查看日期及日期对应总数


        if page:
            try:
                currentPage = int(page.encode('utf-8'))
                nextPage = currentPage + 1 if currentPage + 1 <= totalPage else totalPage
                lastPage = currentPage - 1 if currentPage - 1 > 0 else 1
                sql = 'SELECT * FROM blog LIMIT %d, %d;' %(currentPage*perPage - perPage,currentPage*perPage)

                a = self.query(sql)
                self.render('archives.html', date=date,identies=identies, archives=a, lastPage=lastPage, currentPage=currentPage, nextPage=nextPage)
            except:
                self.write_error(404)
        else:
            sql = 'SELECT * FROM blog LIMIT %d, %d;' %(currentPage*perPage - perPage,currentPage*perPage)
            nextPage = currentPage + 1 if currentPage + 1 <= totalPage else totalPage
            lastPage = currentPage - 1 if currentPage - 1 > 0 else 1
            cad = self.query(sql)
            self.render('archives.html', identies=identies,date=date, archives=cad, lastPage=lastPage, currentPage=currentPage,nextPage=nextPage)

class CategoryHandler(BaseHandler):
    def get(self, cate=''):
        sql1 = 'select identity, COUNT(*) from blog GROUP BY identity;'
        identies = self.query(sql1)
        sql2 = 'SELECT date, COUNT(*) from blog GROUP BY date;'
        Date = self.query(sql2)
        if cate:
                sql = "SELECT * FROM blog WHERE identity='%s';" % cate
                results = self.query(sql)
                print results
                self.render('category.html',results=results, identies=identies, Date=Date)

class DateHandler(BaseHandler):
    def get(self, date=''):
        sql1 = 'SELECT date, COUNT(*) from blog GROUP BY date;'
        Date = self.query(sql1)
        sql2 = 'select identity, COUNT(*) from blog GROUP BY identity;'
        identies = self.query(sql2)
        print Date
        if date:
            print date,type(date)
            sql = "SELECT * FROM blog WHERE date='%s';" % date
            results = self.query(sql)
            self.render('date.html',results=results, Date=Date, identies=identies)

class EssayHandler(BaseHandler):
    def get(self, Eid=''):
        if Eid:
            try:
                sql = 'SELECT * FROM blog where id=%d;' % int(Eid)
                if sql:
                    #results = yield self.executor.submit(self.query, sql)
                    results = self.query(sql)
                    catalog = fetchcatalog.htmlparser(results[0]['essay'])
                    self.render('page.html', title=results[0]['title'],date = results[0]['date'], essay=results[0]['essay'], view=results[0]['view'],catalog=catalog)
            except:
                self.write_error(404)
        else:
            self.write_error(404)

class SubmitHandler(BaseHandler):
    def get(self):
        self.render('submit.html')
    def post(self, *args, **kwargs):
        '''
        self.get_argument('title') 取出的内容均为unicode,
        MySQLdb.escape_string转义时必须先encode为utf-8

        '''
        Title =  self.get_argument('title')
        Date =  self.get_argument('date')
        Essay =   self.get_argument('essay')
        sql = """insert into blog(title,date, essay) values('%s','%s','%s');""" % (MySQLdb.escape_string(Title.encode('utf-8')),MySQLdb.escape_string(Date.encode('utf-8')),MySQLdb.escape_string(Essay.encode('utf-8')))
        self.exesql(sql)
        self.write('OK')

class AboutHandler(BaseHandler):
    def get(self):
        self.render('about.html')

class AdminHandler(BaseHandler):
    def get(self, Eid=''):
        if Eid:
            sql = 'SELECT * FROM blog WHERE id=%d;' % int(Eid)
            results = self.query(sql)

            self.render('edit.html', results=results)
        else:
            sql = 'SELECT * FROM blog;'
            results = self.query(sql)
            self.render('admin.html', results=results)
    def post(self, *args, **kwargs):
        '''
        self.get_argument('title') 取出的内容均为unicode,
        MySQLdb.escape_string转义时必须先encode为utf-8

        '''
        Title =  self.get_argument('title')
        Date =  self.get_argument('date')
        Essay =   self.get_argument('essay')
        Eid = self.get_argument('ID')
        sql = """UPDATE blog SET title='%s', date='%s', essay='%s' WHERE id=%d;""" % (MySQLdb.escape_string(Title.encode('utf-8')),MySQLdb.escape_string(Date.encode('utf-8')),MySQLdb.escape_string(Essay.encode('utf-8')),int(Eid))
        self.exesql(sql)
        self.write('OK')

class DelHandler(BaseHandler):
    def get(self, Eid):
        sql = 'DELETE FROM blog WHERE id=%d' % int(Eid)
        self.exesql(sql)
        self.redirect('/admin')


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()