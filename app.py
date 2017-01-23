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
            (r'/edit/?', EditHandler),
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
        if page:
            try:
                sql = 'SELECT * FROM blog where id=%d;' % int(page)
                if sql:
                    #results = yield self.executor.submit(self.query, sql)
                    results = self.query(sql)
                    catalog = fetchcatalog.htmlparser(results[0]['essay'])
                    self.render('page.html', title=results[0]['title'],date = results[0]['date'], essay=results[0]['essay'], view=results[0]['view'],catalog=catalog)
            except:
                self.write_error(404)
        else:
            sql = 'SELECT * FROM blog;'
            if sql:
                results = self.query(sql)
            self.render('archives.html', archives=results)

class EditHandler(BaseHandler):
    def get(self):
        self.render('edit.html')
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


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()