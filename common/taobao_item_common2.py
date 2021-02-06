#  淘宝测试脚本

import collections
import functools
import json
import logging
import threading
import time
import traceback
from urllib import parse
import requests
from common import random_utils, ip_proxy_1_1


# 获取host
def get_host():
    host_list = [
        # "192.168.31.19"
        "47.110.145.20:5052",
        "47.110.145.20:5051",
    ]
    return random_utils.get_random_ele_form_list(host_list)


to_json = functools.partial(json.dumps, separators=(',', ':'), ensure_ascii=False)


class CommonLocal(threading.local):
    """
    TaobaoItemCommon 的本地线程池
    """

    def __init__(self):
        # 初始化每个线程的变量
        self.err_cnt = 0
        self.proxies = None


class TaobaoItemCommon(object):
    _THREAD_LOCAL = CommonLocal()
    logger = None

    def __new__(cls, *args, **kwargs):
        if cls.logger is None:
            cls.logger = logging.getLogger(cls.__class__.__name__)
        return super().__new__(cls, *args, **kwargs)

    def extract_data_resp(self, itemId):
        """
        提取接口返回的数据
        :param item_id:  商品ID
        :return: (data,rt_code) 若出现异常，则 data 为 None，

        并返回对应的错误码：
        -1.txt 未知错误，
        100 json 解析失败，
        101 商品已过期，
        102 IP被限制访问。
        103 sign 获取异常
        正常情况是 data 不为空，且 rt_code = 0
        """
        x_t = int(round(time.time()))
        lat, lng = random_utils.get_random_location()
        utdid = random_utils.get_random_string(24)
        umt = random_utils.get_random_string(32)
        devid = random_utils.get_random_string(44)

        exParams = collections.OrderedDict({
            "action": "ipv",
            "countryCode": "CN",
            "cpuCore": "4.txt",
            "cpuMaxHz": "2265600",
            "from": "search",
            "id": itemId,
            "item_id": itemId,
            "latitude": str(lat),
            "list_type": "search",
            "longitude": str(lng),
            "osVersion": "23",
            "phoneType": "Nexus 5.txt",
            "search_action": "initiative",
            "soVersion": "2.txt.0",
            "utdid": utdid
        })

        data = collections.OrderedDict({
            "detail_v": "3.txt.1.txt.1.txt",
            "exParams": to_json(exParams),
            "itemNumId": itemId
        })

        params = collections.OrderedDict({
            "deviceId": devid,
            "appKey": "21646297",
            "api": "mtop.taobao.detail.getdetail",
            "data": to_json(data),
            "utdid": utdid,
            "x-features": "27",
            "ttid": "703304@taobao_android_7.6.0",
            "lng": str(lng),
            "v": "6.0",
            "sid": None,
            "t": x_t,
            "uid": None,
            "lat": str(lat),
        })
        data_ = parse.quote(to_json(params))

        # sign 获取 retry
        sign = None
        i = 0
        while i < 3:
            host = get_host()
            try:
                start = time.time()
                # self.logger.info("【{}】【接口: {}】尝试获取 sign , ".format(itemId, host))
                sign = requests.get("http://{}/?data={}".format(host, data_), timeout=7).json()["data"]
                # self.logger.info("【{}】【接口: {}】获取sign success {} {:.3f}".format(itemId, host, sign, time.time() - start))
                break
            except Exception as e:
                self.logger.error("【{}】【接口:{}】获取sign fail {}".format(itemId, host, str(e)))
                time.sleep(3)
            finally:
                i += 1

        if sign is None:
            self.logger.error("【{}】sign 连续3次获取异常".format(itemId))
            return None, 103

        # headers 搭建
        headers = {}
        headers["x-features"] = "27"
        headers["x-location"] = "{}%2C{}".format(lng, lat)
        headers["user-agent"] = "MTOPSDK%2F3.0.4.txt.7+%28Android%3B6.0.1.txt%3BLGE%3BNexus+5.txt%29"
        headers["x-ttid"] = "703304%40taobao_android_7.6.0"
        headers["cache-control"] = "no-cache"
        headers[
            "a-orange-q"] = "appKey=21646297&appVersion=7.6.0&clientAppIndexVersion=1120190910120003337&clientVersionIndexVersion=1220190910120003337"
        headers["x-appkey"] = "21646297"
        headers["x-nq"] = "WIFI"
        headers["content-type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        headers["x-pv"] = "5.txt.1.txt"
        headers["x-t"] = "{}".format(x_t)
        headers["x-app-ver"] = "7.6.0"
        headers["f-refer"] = "mtop"
        headers["x-nettype"] = "WIFI"
        headers["x-utdid"] = utdid
        headers["x-umt"] = umt
        headers["x-devid"] = devid
        headers["x-sign"] = sign
        headers["Host"] = "trade-acs.m.taobao.com"
        headers["Accept-Encoding"] = "gzip"
        headers["Connection"] = "Keep-Alive"
        url = 'http://trade-acs.m.taobao.com/gw/mtop.taobao.detail.getdetail/6.0/?data={}'.format(
            parse.quote(to_json(data)))

        start = time.time()
        res = self.get_requests(url, headers)
        end = time.time()
        # self.logger.info("【{}】请求耗时: {:.3f}".format(itemId, end - start))

        if not res:
            return None, -1

        # self.logger.info("【{}】输出内容: {}".format(itemId, res.text[:100 if len(res.text) >= 100 else len(res.text)]))

        try:
            data = res.json()["data"]
        except json.decoder.JSONDecodeError as e:
            self.logger.warning('json解析失败，原始数据>>> {}'.format(res.text[:100 if len(res.text) >= 100 else len(res.text)]))
            return None, 100

        if data:
            if not data.get('apiStack'):
                rt_code = -1
                if data.get('trade') and 'expired' in data.get('trade').get('redirectUrl'):
                    rt_code = 101
                elif data.get('url') and 'https://h5api.m.taobao.com:443' in data.get('url'):
                    rt_code = 102
                    self._THREAD_LOCAL.proxies = ip_proxy_1_1.get_proxy()
                return None, rt_code

            try:
                api_value = data.get('apiStack')[0].get('value')
                if api_value:
                    api_data = json.loads(api_value)
                    data.get('item')['sellCount'] = api_data.get('item').get('sellCount')
                    data.get('item')['vagueSellCount'] = api_data.get('item').get('vagueSellCount')
                    data['skuCore'] = api_data.get('skuCore')
                    data['weappData'] = api_data.get('weappData')
                    data['trade'] = api_data.get('trade')
                    data['price'] = api_data.get('price')
                    data['extendedData'] = api_data.get('extendedData')
                    data['presale'] = api_data.get('vertical').get('presale')
                    data['trade_state'] = api_data.get('trade')
                data.pop('apiStack')
                data.pop('resource')
            except Exception as e:
                self.logger.error("【{}】解析异常，打印异常栈 {}".format(itemId, traceback.format_exc()))
                self.logger.error("【{}】解析失败 {}".format(itemId, data))

        return data, 0

    def get_requests(self, url, headers, retry_time=0):
        if not self._THREAD_LOCAL.proxies:
            self._THREAD_LOCAL.proxies = ip_proxy_1_1.get_proxy()

        request_fail = True  # 请求异常标识，如果请求正常返回(达到预期要求)，则该标识为 False
        # self.logger.info('当前代理为%s' % self._THREAD_LOCAL.proxies)
        response = None
        try:
            response = requests.get(url, headers=headers, proxies=self._THREAD_LOCAL.proxies, timeout=30)
        except requests.exceptions.ConnectionError as e:
            self.logger.error('ConnectionError,get_brand_product_id proxies again,{}'.format(e))
            self._THREAD_LOCAL.err_cnt = self._THREAD_LOCAL.err_cnt + 1
            self._THREAD_LOCAL.proxies = ip_proxy_1_1.get_proxy()
        except requests.exceptions.ReadTimeout as e:
            self.logger.error('Read timeout'.format(e))
        else:
            # 如果需要登陆,更换ip
            if 'https://login.m.taobao.com/login.htm' in response.text \
                    or 'FAIL_SYS_USER_VALIDATE' in response.text \
                    or '哎哟喂,被挤爆啦,请稍后重试' in response.text:
                self.logger.info('需要登陆，更换IP吧')
                self._THREAD_LOCAL.proxies = None
                self.logger.info('登陆info {}'.format(response.text))
            else:
                request_fail = False
        if request_fail and retry_time < 5:
            # 请求失败，再次发送请求
            retry_time += 1
            self.logger.info('try again time: {}'.format(retry_time))
            return self.get_requests(url, headers, retry_time)
        return response

    def get_request_err_cnt(self):
        """获取接口请求失败的次数"""
        return self._THREAD_LOCAL.err_num


if __name__ == '__main__':
    TaobaoItemCommon().extract_data_resp("578717294140")
    # print(get_host())
