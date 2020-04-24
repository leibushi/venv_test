# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/2.txt 15:56
# @Author  : Mqz
# @FileName: tools.py

# -*- coding:utf-8 -*-

import requests
import json
import random
import datetime
import os
import time
import hashlib
import string
import base64
import execjs

import re

gIpLink = ''
gDialName = ''
gDialAccount = ''
gDialPasswd = ''
openDebug = False
gIpList = []

gStatusCode = ''
gUsername = ''

header = {'User-Agent': 'Mozilla/5.txt.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.186 Safari/537.36'}


def dict2proxy(dic):
    url = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
    return {'http': url, 'https': url}


# @函数介绍： 检验Ip是否是好的
# @返回值： ip是好的/坏的: True/false
# @data: 20180801
def check_ip(ipDict):
    try:
        proxie = dict2proxy(ipDict)
        # printStr(proxie)
        if ipDict['type'] == 'https':
            url = 'https://www.ipip.net/'
        else:
            # url = "http://www.discuz.net/forum.php"
            url = 'http://www.lvye.cn/'
        r = requests.get(url, headers=header, proxies=proxie, timeout=15)
        r.raise_for_status()
        isOk = True
    except Exception as e:
        printStr('经过测试IP无效...')
        isOk = False
    else:
        printStrDebug('经过测试，IP有效...')
        # printStr(ipDict)
    return isOk


# @函数介绍： 获取一个可用的代理Ip
# @返回值： 可用的代理Ip
# @data: 20180801
# freeProxieIpGet()
def getProxieIp():
    cycleFlag = True
    count = 0
    # 打开代理ip文件
    with  open('数据文件夹\proxies.json', 'r') as file:
        jsonStr = file.read()
    dataList = json.loads(jsonStr)  # data 是个list

    listLen = len(dataList)
    maxCount = listLen + 5
    if listLen == 0:
        printStr('proxies.json文件中没有可用ip....')
        return 'null'
    printStr('可用ip个数：%d' % listLen)
    # 读取dict格式的ip
    while cycleFlag == True:
        index = random.randint(0, listLen - 1)  # 随机生成一个Ip
        printStr('随机生成第%d个ip' % index)
        ipDict = dataList[index]
        flag = check_ip(ipDict)
        if flag == True:
            cycleFlag = False
        if count > maxCount:  # 如果循环次数超过maxCount次，则暂停循环
            cycleFlag = False
            ipDict = 'null'
        count = count + 1

    return ipDict


# @函数介绍： 格式化打印输出
# @返回值： 无
# @data: 20180807
def printStr(str):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    print('[%s]>>>>%s' % (nowTime, str))


def printStrDebug(str):
    if openDebug == True:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
        print('[%s]>>>>%s' % (nowTime, str))
    else:
        pass


# @函数介绍： 检测代理IP地址 全局变量是否已经设置
# @返回值： True/False
# @data: 20180810 stefan1240
def payPorxieIpSettingCheck():
    global gIpLink
    if gIpLink == '':
        return False
    else:
        return True


# 功能未完成
def payPorxieIpLinkMake(httpType):
    if gIpLink == '':
        printStr('IP代理链接为空...')
        return 'null'


# @函数介绍： 付费代理Ip池清零
# @返回值：无
# @data: 20180813,stefan1240
def payProxieIpsClear():
    global gIpList
    gIpList = []
    return


# @函数介绍： 付费代理Ip池设定
# @返回值：无
# @data: 20180809,stefan1240
def payProxieIpsUpdate(httpType):
    global gIpList
    global gIpLink
    # 初始值判断
    if gIpLink == '':
        return
        # 判断是哪个平台的代理IP
    if 'zhimacangku' in gIpLink:  #
        # 判断是需要哪种代理ip
        if httpType == 'http':
            if 'port=2.txt' in gIpLink:  # port  代表IP协议（1.txt:HTTP 2.txt:SOCK5 11:HTTPS ）
                gIpLink = gIpLink.replace('port=2.txt', 'port=1.txt')
            if 'port=11' in gIpLink:
                gIpLink.replace('port=3.txt', 'port=1.txt')
        else:  # https
            if 'port=1.txt' in gIpLink:  # port  代表IP协议（1.txt:HTTP 2.txt:SOCK5 11:HTTPS ）
                gIpLink.replace('port=1.txt', 'port=2.txt')
            if 'port=11' in gIpLink:
                gIpLink.replace('port=11', 'port=2.txt')
        # 修改返回IP的数据格式，这里使用txt
        if 'type=2.txt' in gIpLink:  # type数据格式（1TXT 2JSON 3html）
            gIpLink = gIpLink.replace('type=2.txt', 'type=1.txt')
        if 'type=3.txt' in gIpLink:
            gIpLink.replace('type=3.txt', 'type=1.txt')
        if 'num=1.txt' in gIpLink:  # 一次性获取的IP个数设置为20
            gIpLink = gIpLink.replace('num=1.txt', 'num=20')
        # 获取一批量ip，并存于全局变量
        r = requests.get(gIpLink)
        ipStr = r.text
        # IP数据处理
        if 'false' in ipStr:  # 获取太频繁
            printStr('代理平台返回结果：%s' % ipStr)
            return
        elif 'balde' in ipStr:  # 欠费了，直接返回False
            printStr('代理IP欠费了，请到相应平台续费')
            return
        else:
            tmpIpList = ipStr.splitlines()  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
            for strs in tmpIpList:
                tmpIpDict = {}
                if strs.count(':') > 1:
                    printStr('IP代理格式设置不正确,请核对.')
                    return
                if ":" not in strs:
                    printStr('可能是IP代理格式设置不正确，返回结果请设置为txt格式.')
                    return
                ip, port = strs.split(':')
                tmpIpDict['ip'] = ip
                tmpIpDict['port'] = port
                tmpIpDict['type'] = httpType
                # printStrDebug(tmpIpDict)
                gIpList.append(tmpIpDict)
    elif 'xdaili' in gIpLink:  # 讯代理    可以直接按照以下格式组装所需的API链接:http://api.xdaili.cn/xdaili-api/greatRecharge/getGreatIp?spiderId=xx&orderno=xx&returnType=2&count=xx
        if 'spiderId' in gIpLink:
            p = gIpLink.find('spiderId') + len('spiderId=')
            spiderId = gIpLink[p: gIpLink.find('&', p)]
        if 'orderno' in gIpLink:
            p = gIpLink.find('orderno') + len('orderno=')
            orderno = gIpLink[p: gIpLink.find('&', p)]
        fullLink = 'http://api.xdaili.cn/xdaili-api/greatRecharge/getGreatIp?spiderId=' + spiderId + '&orderno=' + orderno + '&returnType=1.txt&count=15'
        # 获取一批量ip，并存于全局变量
        r = requests.get(fullLink)
        ipStr = r.text
        if 'ERRORCODE' in ipStr:
            p = gIpLink.find('ERRORCODE') + len('ERRORCODE":"')
            replyCode = gIpLink[p: gIpLink.find('"', p)]
            if (replyCode == '10036') | (replyCode == '10038') | (replyCode == '10055'):
                printStr('提取代理IP太频繁，请按规定频率提取！')
            if replyCode == '10032':
                printStr('今日代理IP提取已达上限，请隔日提取或额外购买')
        else:
            tmpIpList = ipStr.splitlines()  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
            for strs in tmpIpList:
                tmpIpDict = {}
                if strs.count(':') > 1:
                    printStr('IP代理格式设置不正确,请核对.')
                    return
                if ":" not in strs:
                    printStr('可能是IP代理格式设置不正确，返回结果请设置为txt格式.')
                    return
                ip, port = strs.split(':')
                tmpIpDict['ip'] = ip
                tmpIpDict['port'] = port
                tmpIpDict['type'] = httpType
                # printStrDebug(tmpIpDict)
                gIpList.append(tmpIpDict)

    else:  # 别的类型平台
        # 获取一批量ip，并存于全局变量
        r = requests.get(gIpLink)
        ipStr = r.text
        printStr(ipStr)
        # IP数据处理
        if 'false' in ipStr:  # 获取太频繁
            printStr('获取IP太过频繁，平台给予拒绝...')
            time.sleep(2)
            r = requests.get(gIpLink)
            ipStr = r.text
        elif 'balde' in ipStr:  # 欠费了，直接返回False
            printStr('代理IP欠费了，请到相应平台续费')
            return
        else:
            tmpIpDict = {}
            tmpIpList = ipStr.splitlines()  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
            for strs in tmpIpList:
                if ":" not in strs:
                    printStr('IP代理格式设置不正确，返回结果请设置为txt格式.')
                    return
                ip, port = strs.split(':')
                tmpIpDict['ip'] = ip
                tmpIpDict['port'] = port
                tmpIpDict['type'] = httpType

                gIpList.append(tmpIpDict)
    # printStrDebug('gIpList:%s'%gIpList)
    return


# @函数介绍： 付费代理Ip获取
# @返回值： isGetIpSucess,  tmpIpDict
# @data: 20180809,stefan1240
def payProxieIpGet(httpType):
    isGetIpSucess = False
    tmpIpDict = {}
    ret = False

    while ret == False:
        if len(gIpList) == 0:
            payProxieIpsUpdate(httpType)
        if len(gIpList) == 0:
            isGetIpSucess = False
            break
        tmpIpDict = gIpList.pop()  # 弹出一个IP,
        ret = check_ip(tmpIpDict)
        if ret == True:
            isGetIpSucess = True

    return isGetIpSucess, tmpIpDict


# @函数介绍： 付费代理Ip获取
# @返回值： 返回一个可用的dictIp
# @data: 20180809,stefan1240
def payProxieIpGet_old(httpType):
    global gIpLink
    isSucess = False
    isGetIpSucess = True
    iCirclMax = 50  # 最多循环5次获取
    circleIndex = 0
    gIpLink = 'http://webapi.http.zhimacangku.com/getip?num=1.txt&type=1.txt&pro=&city=0&yys=0&port=1.txt&pack=25657&ts=0&ys=0&cs=0&lb=1.txt&sb=0&pb=4.txt&mr=1.txt&regions='
    """  Ip的格式是这样的：
    http://webapi.http.zhimacangku.com/getip?num=1.txt&type=1.txt&pro=&city=0&yys=0&port=1.txt&time=1.txt&ts=0&ys=0&cs=0&lb=1.txt&sb=0&pb=4.txt&mr=1.txt&regions=
    """
    ipDict = {}

    while isSucess == False:
        if circleIndex > iCirclMax:
            isGetIpSucess = False
            break;
        circleIndex = circleIndex + 1

        r = requests.get(gIpLink)
        ipStr = r.text
        printStr('get:%s' % ipStr)
        if 'false' in ipStr:  # 获取太频繁
            isSucess = False
            time.sleep(1)
        elif 'balde' in ipStr:  # 欠费了，直接返回False
            isGetIpSucess = False
            break
        else:
            ipStr = ipStr.strip('\r\n')
            ip, port = ipStr.split(':')
            ipDict['ip'] = ip
            ipDict['port'] = port
            ipDict['type'] = httpType
            # ret = True
            ret = check_ip(ipDict)
            if ret == True:
                isSucess = True
            else:
                isSucess = False
    return isGetIpSucess, ipDict


# @函数介绍： 付费IP代理链接设置
# @返回值： 成功/失败： True/False
# @data: 20180809, stefan1240
def payPorxieIplinkSet(ipAddrsLink):
    global gIpLink
    if ipAddrsLink == '':
        printStr('未输入代理IP链接，请输入有效的IP代理链接...')
        return False
    elif not ipAddrsLink.startswith(('http://', 'https://')):
        printStr('你输入的IP代理链接格式不对，请检查一下格式...')
        return False
    else:
        gIpLink = ipAddrsLink
    return True


# @函数介绍： 宽带参数设置
# @返回值： 成功/失败： True/False
# @data: 20180809, stefan1240
def dialParaSet(dialName, dialAccount, dialPasswd):
    global gDialName
    global gDialAccount
    global gDialPasswd
    gDialName = dialName
    gDialAccount = dialAccount
    gDialPasswd = dialPasswd
    return True


# @函数介绍： 宽带连接
# @返回值： 成功/失败： True/False
# @data: 20180809, stefan1240
def dialConnect():
    global gDialName
    global gDialAccount
    global gDialPasswd
    if gDialName == '':
        return False
    cmdStr = 'rasdial %s %s %s' % (gDialName, gDialAccount, gDialPasswd)
    ret = os.system(cmdStr)
    if ret == 0:
        isSucess = True
    else:
        isSucess = False
        printStr('拨号失败，错误代码:%s' % ret)
    return isSucess


# @函数介绍： 宽带断开
# @返回值： 成功/失败： True/False
# @data: 20180809, stefan1240
def dialDisconnect():
    global gDialName
    cmdStr = 'rasdial %s /disconnect' % gDialName
    ret = os.system(cmdStr)
    if ret == 0:
        isSucess = True
    else:
        isSucess = False
    return isSucess


# @函数介绍： 宽带重连
# @返回值： 无
# @data: 20180809, stefan1240
def dialReconnect():
    ret = dialDisconnect()
    if ret == True:
        time.sleep(3)
        dialConnect()
        time.sleep(1)


# @函数介绍： 随机生成n个中文字符
# @返回值： 中文字符串
# @data: 20180814, stefan1240
def randomChineseGet(num):
    strs = ''
    for i in range(num):
        val = random.randint(0x4e00, 0x9fbf)
        strs = strs + chr(val)
    return strs


def randomChar(num):
    return ''.join(random.choice(string.ascii_letters) for x in range(num))


def randomInt(num):
    strs = ''
    for i in range(num):
        number = random.randint(1, 9)
        strs = strs + str(number)
    return strs


# @函数介绍： md5加密
# @输入： 字符串型
# @返回值： md5加密后的字符串
def genearteMD5(strs):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(strs.encode(encoding='utf-8'))

    return hl.hexdigest()


# @函数介绍： sh256加密
# @输入： 字符串型
# @返回值： sh256加密后的字符串
def genearteSH256(strs):
    sha256 = hashlib.sha256()
    sha256.update(strs.encode('utf-8'))
    return sha256.hexdigest()


# @函数介绍： base64加密
# @输入： 字符串型
# @返回值： base64加密后的字符
def genearteBase64(strs):
    strEncode = base64.b64encode(strs.encode('utf-8'))
    return strEncode.decode()


# @函数介绍： 新浪web加密某个字段需要调用JS代码
# @输入： servertime,  nonce,  passwd,  pubkey
# @返回值： base64加密后的字符
def xinlanJsEcode(servertime, nonce, passwd, pubkey):
    xinlanJsStr = xinlanJsStrGet()
    handle = execjs.compile(xinlanJsStr)
    ret = handle.call('Getsp', servertime, nonce, passwd, pubkey)
    return ret


# @data: 20180814, stefan1240
# dic = {'ip':'182.244.109.222', 'port':'4230', 'type':'https'}
# check_ip(dic)

# ------------------------易游对接相关API---------------------------------------------------------------
# @函数介绍：从配置文件获取登录用户信息相关
# @输入值:
# @返回值： gStatusCode， gUsername
# @data: 201808022
def loingAccountInfoGet():
    global gStatusCode
    global gUsername

    file = open('系统文件(勿动)\para.ini', 'r')
    for line in file.readlines():
        line = line.strip('\n')
        if '<registerInfo>' in line:
            para = re.findall("<registerInfo>(.+?)<registerInfo>", line)
            gUsername, passwd = para[0].split(':')
        if '<retCodeInfo>' in line:
            para = re.findall("<retCodeInfo>(.+?)<retCodeInfo>", line)
            gStatusCode = para[0]
    file.close()


# @函数介绍：获取用户状态
# @输入值:  statusCode:登录成功后返回的状态码，  userName:用户名
# @返回值： 成功的返回1或者错误代码，代码含义：http://dev.eydata.net/webapi/errorlist
# @data: 201808021
def checkUserStatus():
    global gStatusCode
    global gUsername

    url = 'https://w.eydata.net/aec651134b90f1ab'
    data = {
        "StatusCode": gStatusCode,
        "UserName": gUsername
    }
    r = requests.post(url, data)
    return r.text


# @函数介绍：退出接口
# @输入值:
# @返回值： 成功的返回1或者错误代码，代码含义：http://dev.eydata.net/webapi/errorlist
# @data: 201808021
def logOut():
    statusCode = ''
    userName = ''

    file = open('系统文件(勿动)\para.ini', 'r')
    for line in file.readlines():
        line = line.strip('\n')
        if '<registerInfo>' in line:
            para = re.findall("<registerInfo>(.+?)<registerInfo>", line)
            userName, passwd = para[0].split(':')
        if '<retCodeInfo>' in line:
            para = re.findall("<retCodeInfo>(.+?)<retCodeInfo>", line)
            statusCode = para[0]
    file.close()

    url = 'https://w.eydata.net/a8a66a6329265b37'
    data = {
        "StatusCode": statusCode,
        "UserName": userName
    }
    r = requests.post(url, data)
    return r.text


# -----------------------------------------------------------------------------------
# @函数介绍：把代理IP链接写入到配置文件
# @输入值:  statusCode:登录成功后返回的状态码，  userName:用户名
# @返回值： 成功的返回1或者错误代码，代码含义：http://dev.eydata.net/webapi/errorlist
# @data: 201808021
def writeIpLinkIntoFile():
    global gIpLink
    needWrite = True
    if gIpLink == '':
        printStr('代理IP链接为空,停止写入到配置文件...')
    ipAddresLink = gIpLink
    # 写入配置文件
    strs = '<IplinkInfo>%s<IplinkInfo>\n' % ipAddresLink
    # 使用w模式会将原本的文件清空/覆盖。可以先用读（r）的方式打开，写到内存中,然后再用写（w）的方式打开。
    with open('系统文件(勿动)\para.ini', 'r', encoding="utf-8") as file:
        lines = file.readlines()
    with open('系统文件(勿动)\para.ini', 'w', encoding="utf-8") as file:
        for line in lines:  # 替换
            if '<IplinkInfo>' in line:
                s = line.replace(line, strs)
                file.write(s)
                needWrite = False
            else:
                file.write(line)
    printStrDebug('needWrite=%s' % needWrite)
    if needWrite == True:  # 首次写入
        with open('系统文件(勿动)\para.ini', 'a+', encoding="utf-8") as file:
            file.write(strs)


"""
articleBody ='hello'
articleTitle = 'hello'
deviceid = 'ab56b4d92b40713acc5af89985d4b786'
uid = '6611942773'
str1 ="act=1.txt&allow_comment=1.txt&allow_repost=1.txt&appid=2.txt&appver=3.txt.0.2.txt&article_body=" + articleBody + "&article_title="+articleTitle 
str2 = "&chno=515_112&class_id=0&deviceid=" + deviceid + "&is_secret=0&is_to_weibo=0&login_uid=" +uid 
str3 = "&signkey=e3eb41c951f264a6daa16b6e4367e829&sort_id=117"
body = str1 + str2 + str3
sign = genearteSH256(body)
print(sign)
"""
