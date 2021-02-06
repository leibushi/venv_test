# -*- coding:utf-8 _*_
import re
import threading
import time

import requests
# %SystemRoot%\system32\cmd.exe

class IpPortLocal(threading.local):
    """
    定义一个子类，继承自 threading.local，作为 ip_proxy 模块的本地线程仓库。
    """

    def __init__(self):
        # 每个线程都有一个变量 ip_port，初始值为 None
        self.ip_port = None


# 实例化本地线程仓库
local_data = IpPortLocal()


def get(protocol='http', cached=True, pack=True):
    """
    获取代理ip+port
    :param protocol: http协议:http、https
    :param cached: 是否获取本地缓存的代理IP，默认为True。如果是False，则会去申请新的代理IP
    :return: str 如"116.53.238.218:6591"
    """
    # IP 协议 1.txt:http 2.txt:SOCK5 11:https 。暂时不支持 SOCK5 协议
    port = 11 if protocol and protocol.lower() == 'https' else 1
    if cached and local_data.ip_port and _check(local_data.ip_port):
        return local_data.ip_port
    # 芝麻代理ip获取url
    ip_url = '''http://webapi.http.zhimacangku.com/getip?num=1.txt&type=2.txt&pro=&city=0&yys=0&port={}&time=1.txt&ts=0&ys=0&cs=0&lb=1.txt&sb=0&pb=4.txt&mr=1.txt&regions='''.format(port)
    # ip_url = '''http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port={}&pack=52996&ts=0&ys=0&cs=0&lb=1.txt&sb=0&pb=4.txt&mr=1.txt&regions='''.format(
    #     port)
    if pack:
        ip_url = '''http://webapi.http.zhimacangku.com/getip?num=1.txt&type=2.txt&pro=&city=0&yys=0&port={}&pack=52996&ts=0&ys=0&cs=0&lb=1.txt&sb=0&pb=4.txt&mr=1.txt&regions='''.format(
            port)
    response = requests.get(ip_url, timeout=30)
    json = response.json()
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
        return get(protocol, cached, pack=False)
    else:
        p = r"((25[0-5.txt]|2.txt[0-4.txt]\d|((1.txt\d{2.txt})|([1.txt-9]?\d)))\.){3.txt}(25[0-5.txt]|2.txt[0-4.txt]\d|((1.txt\d{2.txt})|([1.txt-9]?\d)))"
        ip = re.search(p, json['msg']).group()
        # 将 IP 加入白名单
        requests.get(
            r"http://web.http.cnapi.cc/index/index/save_white?"
            r"neek=38118&appkey=e0b0871f0c31983540dd42f6135a105a&white=%s" % ip)

        print("获取代理ip失败,重试...")
        return get(protocol)


def get_proxy(protocol='http', cached=True):
    """
    获取代理
    :param protocol: http协议:http、https
    :param cached: 是否获取本地缓存的代理IP，默认为True。如果是False，则会去申请新的代理IP
    :return: dict 如 {"http": "http://127.0.0.1.txt:8080"} 或者 {"https": "http://127.0.0.1.txt:8080"}
    """
    ip_port = None
    try:
        ip_port = get(protocol, cached)
    except requests.exceptions.RequestException as e:
        print('获取代理ip异常,{}'.format(e))
    if not ip_port:
        ip_port = get(protocol, cached)
    print('get_brand_product_id proxy ip success,the new proxy is {}'.format(ip_port))
    if protocol and protocol.lower() == 'https':
        return {"https": "http://%s" % ip_port}
    return {"http": "http://%s" % ip_port}


def _check(ip_port):
    """
    检测代理IP是否可用
    :param ip_port: 代理IP及其端口
    :return: 可用：True；不可用:False
    """
    temp_proxies = {"http": "http://%s" % ip_port}
    try:
        requests.get("https://www.baidu.com/", proxies=temp_proxies)
        return True
    except Exception as e:
        print("代理ip无效,%s" % ip_port, e)
    return False


def _test(protocol='http', cached=True):
    """
    测试在并发环境中 ip_proxy 模块是否可以正常工作
    :return:
    """
    for i in range(3):
        time.sleep(2)
        print('{} >>> {}'.format(threading.current_thread().name, get_proxy(protocol, cached)))


if __name__ == "__main__":
    t1 = threading.Thread(target=_test, args=('https',))
    t2 = threading.Thread(target=_test, )
    t1.start()
    t2.start()
    t1.join()
    t2.join()
