#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-1-22 下午8:35
# @Author  : Sugare
# @mail    : 30733705@qq.com
# @File    : fetchcatalog.py
# @Software: PyCharm
import requests
from HTMLParser import HTMLParser


class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None

        if tag == 'h3' and _attr(attrs, 'essay-title'):
            movie = {}
            movie['essay-title'] = _attr(attrs, 'essay-title')
            #movie['director'] = _attr(attrs, 'data-director')
            #movie['duration'] = _attr(attrs, 'data-dutation')
            #movie['title'] = _attr(attrs, 'data-title')
            #movie['rate'] = _attr(attrs, 'data-rate')
            self.movies.append(movie)


def urlparser(url):
    headers = {}
    req = requests.get(url)
    s = req.text
    htmlparser(s)

def htmlparser(html):
    myparser = Myparser()
    myparser.feed(html)
    myparser.close()
    return myparser.movies

html = """
<h3 essay-title='一、集群的定义'><a href="一、集群的定义">一、集群的定义</a></h3>
<p style="letter-spacing:2px;font-family:'楷体';">12345</p>

<h3 essay-title='二、集群的基本特点'><a href="二、集群的基本特点">二、集群的基本特点</a></h3>
<p style="background-color: rgba(128,128,128,0.15);font-style: inherit;letter-spacing:2px;font-family: '微软雅黑';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.高性能</p>

<h3 essay-title='三、集群的分类'><a href="三、集群的分类">三、集群的分类</a></h3>
<p style="font: 12px/1.5 Tahoma,Helvetica,Arial,'宋体',sans-serif;"><a href="#">负载均衡集群（LB）</a></p>

"""


if __name__ == '__main__':
    #url = 'https://movie.douban.com/'
    #movies = movieparser(url)
    #for each in movies:
    #    print('%(title)s|%(rate)s|%(actors)s|%(director)s|%(duration)s' % each)
    catalog_total = htmlparser(html)
    print catalog_total