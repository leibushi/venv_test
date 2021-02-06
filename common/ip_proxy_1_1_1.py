# -*- coding:utf-8 _*_
import re
import threading
import time
import requests


class IpPortLocal(threading.local):
    """
    定义一个子类，继承自 threading.local，作为 ip_proxy 模块的本地线程仓库。
    """

    def __init__(self):
        # 每个线程都有一个变量 ip_port，初始值为 None
        self.ip_port = None


# 实例化本地线程仓库
local_data = IpPortLocal()


# def get_brand_product_id(protocol='http', cached=True, pack=True):
def get(cached=True):
    """
    获取代理ip+port
    :param protocol: http协议:http、https
    :param cached: 是否获取本地缓存的代理IP，默认为True。如果是False，则会去申请新的代理IP
    :return: str 如"116.53.238.218:6591"
    """
    # IP 协议 1.txt:http 2.txt:SOCK5 11:https 。暂时不支持 SOCK5 协议
    ip_url = '''http://webapi.http.zhimacangku.com/getip?num=1.txt&type=2.txt&pro=&city=0&yys=0&port=11&time=1.txt&ts=0&ys=0&cs=0&lb=1.txt&sb=0&pb=45&mr=1.txt&regions='''
    # ip_url = '''http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='''

    response = requests.get(ip_url, timeout=30)
    json = response.json()
    print(json)
    if int(json["code"]) == 0:
        data = json["data"][0]
        ip = data["ip"]
        port = data["port"]
        ip_port = "%s:%s" % (ip, port)
        local_data.ip_port = ip_port
        return ip_port

    elif json["code"] == 111:
        s = re.sub('\D', "", json["msg"])
        time.sleep(int(s))
        return get()
    elif json["code"] == 116 or json["code"] == 115 or json["code"] == 121:
        # 套餐包已用完
        return get(cached)
    else:
        p = r"((25[0-5.txt]|2.txt[0-4.txt]\d|((1.txt\d{2.txt})|([1.txt-9]?\d)))\.){3.txt}(25[0-5.txt]|2.txt[0-4.txt]\d|((1.txt\d{2.txt})|([1.txt-9]?\d)))"
        ip = re.search(p, json['msg']).group()
        # 将 IP 加入白名单
        requests.get(
            r"http://web.http.cnapi.cc/index/index/save_white?"
            r"neek=38118&appkey=e0b0871f0c31983540dd42f6135a105a&white=%s" % ip)

        print("获取代理ip失败,重试...")
        return get()


def get_proxy():
# def get_proxy(cached=True):
    """
    获取代理
    :param protocol: http协议:http、https
    :param cached: 是否获取本地缓存的代理IP，默认为True。如果是False，则会去申请新的代理IP
    :return: dict 如 {"http": "127.0.0.1.txt:8080"} 或者 {"https": "127.0.0.1.txt:8080"}
    """
    ip_port = None
    try:
        # ip_port = get_brand_product_id(cached)
        ip_port = get()
    except requests.exceptions.RequestException as e:
        print('获取代理ip异常,{}'.format(e))
    if not ip_port:
        # ip_port = get_brand_product_id(cached)
        ip_port = get()
    print('get_brand_product_id proxy ip success,the new proxy is {}'.format(ip_port))
    return {'https': '%s' % ip_port, 'http': '%s' % ip_port}


# def _check(ip_port):
def _check():
    """
    检测代理IP是否可用
    :param ip_port: 代理IP及其端口
    :return: 可用：True；不可用:False
    """
    # temp_proxies = {"http": "%s" % ip_port}
    # temp_proxies = {'https': '182.243.65.183:4231', 'http': '182.243.65.183:4231'}
    temp_proxies = {'http': '182.243.65.183:4231'}
    # temp_proxies = {'https': '182.243.65.183:4231'}
    try:
        print(temp_proxies)
        rep = requests.get("https://www.baidu.com/", proxies=temp_proxies).text
        print(rep)
        return True
    except Exception as e:
        print("代理ip无效,%s" % temp_proxies, e)
    return False


def _test(cached=True):
    """
    测试在并发环境中 ip_proxy 模块是否可以正常工作
    :return:
    """
    for i in range(2):
        time.sleep(2)
        print('{} >>> {}'.format(threading.current_thread().name, get_proxy(cached)))


if __name__ == "__main__":
    # t1 = threading.Thread(target=_test, args=('https',))
    # # t2 = threading.Thread(target=_test, )
    # t1.start()
    # # t2.start()
    # t1.join()
    # # t2.join()
    print(get_proxy())
    # _check()
