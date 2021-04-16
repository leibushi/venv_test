# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 10:16
# @Author  : Mqz
# @FileName: threding3.py
import datetime
import os
import queue
import threading
import time
import random
import requests
from lxml import etree
from common.ip_proxy import get_proxy


'''
采集线程类
'''
class Crawl(threading.Thread):
    # threading.Lock = get_proxy()
    # proxies = get_proxy()
    # 初始化
    def __init__(self,number,req_list,data_list):
        # 调用Thread 父类方法
        super(Crawl,self).__init__()
        # 初始化子类属性
        self.number = number
        self.req_list = req_list
        self.data_list = data_list
        self.proxies = None
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }

        # 线程启动的时候调用
    def run(self):
        if not self.proxies:
            self.proxies = get_proxy()
        # 输出启动线程信息
        print('启动采集线程%d号' % self.number)
        # 如果请求队列不为空，则无限循环，从请求队列里拿请求url
        while self.req_list.qsize() > 0:
            # 从请求队列里提取url
            url = self.req_list.get()
            print('%d号线程采集：%s' % (self.number,url))
            # 防止请求频率过快，随机设置阻塞时间
            time.sleep(random.randint(1,3))
            # 发起http请求，获取响应内容，追加到数据队列里，等待解析
            response = requests.get(url,headers=self.headers, proxies=self.proxies)
            if response.status_code == 200:
                self.data_list.put(response.text)  # 向数据队列里追加
# 创建文件对

f = open('qichezhijia.json', 'w', encoding='utf-8')
'''
下载图片文件
'''


def downfiles(imglist, carName):
    x = 0  # 计数
    folder = None
    for name in carName:
        folder = './images/1/' + name + '_' + str(x)  # 设置图片保存的路径
    if not os.path.exists(folder):
        # os.makedirs(folder)
        print(folder + ' => 创建成功')
        # 从imglist中遍历拿到单个的imgurl
        for imgurl in imglist:
            # 发起网络请求来下载图片!!!（很重要）
            imgres = requests.get("http:" + imgurl)
            if imgres.status_code == 200:
                # img.content用来返回二进制数据，wb是二进制流写入
                fname = imgurl.split('/')[-1]
                with open(folder + fname, "wb") as f:
                    f.write(imgres.content)
                    x += 1
                    print("下载第", x, "张")
            else:
                print('图片下载失败：', imgres.status_code)
    else:
        pass
        print('路径已创建，请忽略 => ' + carName)
'''
解析线程类
'''
class Parse(threading.Thread):
    # 初始化属性
    def __init__(self,number,data_list,req_thread,f):
        super(Parse ,self).__init__()
        self.number = number                # 线程编号
        self.data_list = data_list          # 数据队列
        self.req_thread = req_thread        # 请求队列，为了判断采集线程存活状态
        self.f = f                          # 获取文件对象
        self.is_parse = True                # 判断是否从数据队列里提取数据
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }

    def run(self):
        print('启动%d号解析线程' % self.number)
        # 无限循环，
        while True:
            # 如何判断解析线程的结束条件
            for t in self.req_thread:           # 循环所有采集线程
                if t.is_alive():                # 判断线程是否存活
                    break
            else:                           # 如果循环完毕，没有执行break语句，则进入else
                if self.data_list.qsize() == 0:             # 判断数据队列是否为空
                    self.is_parse = False                   # 设置解析为False

             # 判断是否继续解析
            if self.is_parse:   # 解析
                try:
                    data = self.data_list.get(timeout=3)            # 从数据队列里提取一个数据
                except Exception as e:      # 超时以后进入异常
                    data = None
                # 如果成功拿到数据，则调用解析方法
                if data is not None:
                    self.parse(data)        # 3.调用页面解析方法
            else:
                break       # 结束while 无限循环
        print('退出%d号解析线程' % self.number)

    # 页面解析函数
    def parse(self,data):
        html = etree.HTML(data)

        # 获取所有车图片的div==/html/body/div[2]/div/div[2]/div[7]/div/div[2]/div[2]
        duanzi_div = html.xpath('/html/body/div[2]/div/div[2]/div[7]/div/div[2]/div[2]')

        for duanzi in duanzi_div:
            # 获取车名
            carName = duanzi.xpath('./ul/li/div/a/text()')
            print('车名：',carName,len(carName))

            # 获取车图==/html/body/div[2]/div/div[2]/div[7]/div/div[2]/div[2]/ul/li[1]/a/img
            imgList= duanzi.xpath('./ul/li/a/img/@src')
            print('图片：',imgList,type(imgList),len(imgList))  #  <class 'list'>
            downfiles(imgList,carName)





def main():
    # 生成请求队列
    req_list = queue.Queue()
    # 生成数据队列 ，请求以后，响应内容放到数据队列里
    data_list = queue.Queue()
    # 创建文件对象
    f = open('qichezhijia.json','w',encoding='utf-8')
    # 循环生成多个请求url
    for i in range(1,10 + 1):  # 10页
        base_url='https://car.autohome.com.cn/pic/series/66-12-p%d.html' % i
        # 加入到请求队列中
        req_list.put(base_url)

    concurrent = 3  # 采集线程数
    conparse = 3  # 解析线程数

    # 生成N个解析线程
    parse_thread = []
    # 生成N个采集线程
    req_thread = []
    for i in range(concurrent):
        t = Crawl(i + 1, req_list, data_list)  # 1.调用创造线程方法
        t.start()
        req_thread.append(t)

    for i in range(conparse):
        t = Parse(i + 1, data_list, req_thread, f)  # 2.创造解析线程方法
        t.start()
        parse_thread.append(t)
    for t in req_thread:
        t.join()
    for t in parse_thread:
        t.join()


if __name__ == '__main__':
    start = time.time()
    main()                  # 运行爬虫程序
    end = time.time()
    spendtime = end - start
    print("用时 " + str(spendtime) + "秒")