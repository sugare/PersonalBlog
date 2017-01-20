#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/20 15:52
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : app.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import os
import tornado.httpserver


#from tornado.options import define, options
#define("port", default=8888, help="run on the given port", type=int)
#define("redis_host", default="127.0.0.1", help="redis host")
# define("redis_port", default=6379, help="redis port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/?', HomeHandler),
            #(r'/archives', ArchivesHandler),
            (r'/archives/?(.*)', ArchivesHandler),
            #(r'/archives?', ArchivesHandler),
            (r'/about?', AboutHandler),
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

class BaseHandler(tornado.web.RequestHandler):
    pass

class HomeHandler(BaseHandler):
    def get(self):
        self.render('home.html')

class ArchivesHandler(BaseHandler):
    def get(self, page=''):
        if page:
            self.render('page.html', page=page)
        else:
            self.render('archives.html')


class AboutHandler(BaseHandler):
    def get(self):
        self.render('about.html')

def main():
    # tornado.options.parse_command_line()
    app = Application()
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(8888)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()