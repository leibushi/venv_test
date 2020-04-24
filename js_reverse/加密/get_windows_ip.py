# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/10 11:31
# @Author  : Mqz
# @FileName: get_windows_ip.py
import os
import socket

def get_window_ip1():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        print(s.getsockname())
        ip = s.getsockname()[0]
        # print(ip)
    finally:
        s.close()

    return ip

def get_window_ip2():
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 需要注意的是，如果本机有多网卡，比如说安装的有虚拟机，则此ip可能是虚拟机VMnet8的ip，而你真正的内网IP可能是物理无线适配器wlan的IP
    ip = socket.gethostbyname(hostname)

    #这种情况下，首先需要获取所有网卡的ip地址，然后人为进行筛选
    ipList = socket.gethostbyname_ex(hostname)
    print(ipList)
    return ipList[2][-1]

def get_window_ip3():
    return [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]

def get_window_ip4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('baidu.com', 0))
    ipaddr = s.getsockname()[0]
    print(ipaddr)
    return ipaddr

get_window_ip1()

get_window_ip2()
get_window_ip4()
# ————————————————
# 版权声明：本文为CSDN博主「hresh」的原创文章，遵循 CC 4.txt.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Herishwater/article/details/100622020