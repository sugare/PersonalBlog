#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/21 21:19
# @Author  : Sugare
# @Site    : 30733705@qq.com
# @File    : test.py
# @Software: PyCharm

import MySQLdb
import markdown2
db = MySQLdb.connect('localhost','root','123456','blog', charset="utf8")


cursor = db.cursor()

# cursor.execute('set names gbk;')
html = """
<h3 essay-title='一、集群的定义'><a href="一、集群的定义">一、集群的定义</a></h3>
<p style="letter-spacing:2px;font-family:'楷体';">工欲善其事必先利其器。把自己要用的工具尽量熟透，我觉得是必须要做的。花了两个星期才把<python标准库>看完，主要是看小说去了，汗。
书有点老,10年的，不过不长，只有329页。到处找了下，貌似都是10/06/07的那本。

讲的并不深入，就是对python的标准模块有个了解，有个大概的印象。基本上每个模块都给了个简单的例子。
还是推荐阅读下，全面了解下python标准模块对于阅读理解各种第三方模块的源码很有帮助。我个人感觉到的就是python还真是强大，各种功能都有，确实是unix管理者和黑客爱的玩意儿。我估计也会在这条路上走的越来越远。
可以搭配着《unix环境高级编程》一起阅读，要不然有些概念是看了完全没有印象的。
只求个大概了解可以去我的博客http://go2live.cn/archives/177159.html</p>

<h3 essay-title='二、集群的基本特点'><a href="二、集群的基本特点">二、集群的基本特点</a></h3>
<p style="background-color: rgba(128,128,128,0.15);font-style: inherit;letter-spacing:2px;font-family: '微软雅黑';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.高性能工欲善其事必先利其器。把自己要用的工具尽量熟透，我觉得是必须要做的。花了两个星期才把<python标准库>看完，主要是看小说去了，汗。
书有点老,10年的，不过不长，只有329页。到处找了下，貌似都是10/06/07的那本。

讲的并不深入，就是对python的标准模块有个了解，有个大概的印象。基本上每个模块都给了个简单的例子。
还是推荐阅读下，全面了解下python标准模块对于阅读理解各种第三方模块的源码很有帮助。我个人感觉到的就是python还真是强大，各种功能都有，确实是unix管理者和黑客爱的玩意儿。我估计也会在这条路上走的越来越远。
可以搭配着《unix环境高级编程》一起阅读，要不然有些概念是看了完全没有印象的。
只求个大概了解可以去我的博客http://go2live.cn/archives/177159.html</p>

<h3 essay-title='三、集群的分类'><a href="三、集群的分类">三、集群的分类</a></h3>
<p style="font: 12px/1.5 Tahoma,Helvetica,Arial,'宋体',sans-serif;">工欲善其事必先利其器。把自己要用的工具尽量熟透，我觉得是必须要做的。花了两个星期才把<python标准库>看完，主要是看小说去了，汗。
书有点老,10年的，不过不长，只有329页。到处找了下，貌似都是10/06/07的那本。

讲的并不深入，就是对python的标准模块有个了解，有个大概的印象。基本上每个模块都给了个简单的例子。
还是推荐阅读下，全面了解下python标准模块对于阅读理解各种第三方模块的源码很有帮助。我个人感觉到的就是python还真是强大，各种功能都有，确实是unix管理者和黑客爱的玩意儿。我估计也会在这条路上走的越来越远。
可以搭配着《unix环境高级编程》一起阅读，要不然有些概念是看了完全没有印象的。
只求个大概了解可以去我的博客http://go2live.cn/archives/177159.html</p>

"""
#sql = """insert into blog(title,date, essay) values('集群的相关内容','2017-01-02','%s');;""" %MySQLdb.escape_string(html)
print (MySQLdb.escape_string(html))
print type(MySQLdb.escape_string(html))
#cursor.execute(sql)
#db.commit()

#db.close()
