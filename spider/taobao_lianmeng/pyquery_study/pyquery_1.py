# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 13:46
# @Author  : Mqz
# @FileName: pyquery_1.py
from pyquery import PyQuery as pq

html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>首页</title>
    </head>
    <body class="item">
        <p class="item" id="username">This is your username</p>
        <p class="item" id="password">This is your password</p>
    </body>
    </html>
'''

html2 = '''
<div id = 'container'>
    <ul class = 'list'>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''
doc = pq(html)
print(doc)
# 获取所有节点的文本内容
print(doc.text())
result = doc('title')
print(result)  # 表示提取<title>节点，结果为：<title>首页</title>
result = doc('.item')  # 可以基于CSS选择器来进行提取，这里表示提取class="item"的所有节点
print('item', result)

result = doc.find('p')  # find()方法会将符合条件的所有节点选择出来，这里表示提取所有<p>节点
print('p', result)
result = doc.find('p').attr('id')  # attr()用于获取节点的属性值，这里表示获取id属性的值，结果为：username
print('id', result)
result = doc.find('p').text()  # text()用于获取节点的文本内容，结果为
print(result)

doc = pq(html2)
print(doc('li'))
# 效果实现一样
print(doc('#container .list li'))
print(doc.find('li'))
li = doc.children()
print(li)
# print(type(li))

li2 = doc.children('.active')
print('li2', li2)
items = doc('.list')
# 找到父节点
container = items.parent()
print(container)

# 兄弟元素
li = doc('.list .item-0.active')
print(li.siblings())
# 遍历
li = doc('.item-0.active')
# 从结果中我们可以看出通过items()可以得到一个生成器，并且我们通过for循环得到的每个元素依然是一个pyquery对象。
lis = doc('li').items()
print(lis)
for li in lis:
    print(li)

# 获取属性 attr(属性名)
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)

# 获取文本
# 我们是需要获取被html标签包含的文本信息,通过.text()就可以获取文本信息
print(a.text())

# 获取html
# 我们通过.html()的方式可以获取当前标签包含的html信息，
li = doc('.item-0.active')
print(li.html())

# DOM 文本操作
# 删除class 名
li.removeClass('active')
print(li)
# 添加属性
li.addClass('active')
print(li)

# 属性名 attr css
# name="link"
# 同样的我们可以通过attr给标签添加和修改属性，
# 如果之前没有该属性则是添加，如果有则是修改
# 我们也可以通过css添加一些css属性，这个时候，标签的属性里会多一个style属性
li.attr('name', 'link')
print(li)
# 增加css样式
li.css('font-size', '14px')
print(li)