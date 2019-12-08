#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# 宋艾衡  2019-12-08 , 16:59

from bs4 import BeautifulSoup

html_doc = """

<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse"s story</b></p>
<p cLass="story">Once upon a time there were three little sisters; and their nanes were
<a href一"http://example.com/elsie" class="sister" id="link1">ELs ie</a>,
<a href="http://example.com/lacie" class="sister" id="Link2">Lacie</a> and
<a href= "http://example.com/tillie" class="sister" id="Link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

# 找到title标签
print(soup.title)

# 获取title标签里的内容
print(soup.title.string)

# 找到p标签
print(soup.p)

# 找到p标签里的class标签
print(soup.p['class'])

# 找到a标签
print(soup.a)

# 找到所有的a标签
print(soup.find_all('a'))


# 找到id为link3的标签
print(soup.find(id="link3"))

# 找到所有a标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 找到文档中所有文本内容
print(soup.get_text)


