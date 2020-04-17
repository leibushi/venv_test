# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 13:39
# @Author  : Mqz
# @FileName: tieba_meitu.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author:Herish
datetime:2019/3/29 14:12
software: PyCharm
description:
'''
import requests
from pyquery import PyQuery as pq
from lxml import etree
import os
from PIL import Image
from io import BytesIO
from hashlib import md5

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1'
}

UNIT_SIZE = 600  # 高
TARGET_WIDTH = 400  # 宽


class BaiduTiebaPhoto:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/p/5033202671'
        self.datas = []
        self.fpath = "D:/360安全浏览器下载\spider_file/1"
        self.new_fpath = "D:/360安全浏览器下载\spider_file/2/"
        self.photoWall_fpath = "E:/PycharmWspace/yeayee/data/baidu_img2.0/photoWall/"

    # 获取页面详情
    def getText(self, url):
        try:
            response = requests.get(url, headers)
            if 200 == response.status_code:
                return response.text
        except:
            return None

    # 提取图片的url
    def dealText(self, url):
        photo_urls = []
        text = self.getText(url)

        # 1,利用lxml进行匹配
        html = etree.HTML(text)
        results = html.xpath('//img[@class="BDE_Image"]/@src')

        # 2利用Pyquery进行匹配
        # doc = pq(text)
        # for i in doc('.BDE_Image').items():
        #     photo_urls.append(i.attr('src'))

        self.datas.extend(results)

    #根据图片二进制数据，利用Image返回图片的宽和高
    def img_size(self, content):
        img = Image.open(BytesIO(content))

        # width,height = img.size
        return img.size

    #根据图片url下载图片
    def saveImg(self, url):
        if not os.path.exists(self.fpath):
            os.mkdir(self.fpath)
        try:
            response = requests.get(url)
            if 200 == response.status_code:
                file_path = '{0}{1}.{2}'.format(self.fpath, md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    if self.img_size(response.content)[0] > 400 and self.img_size(response.content)[1] > 600:  # 图片宽*高大于400*600像素才保存
                        print('尺寸不错，留下了')
                        with open(file_path, 'wb') as fw:
                            fw.write(response.content)
                else:
                    print('Already Download', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image')

    def ResizeImage(self):
        '''图片尺寸大小修改
        :param filein: 图片打开路径
        :param fileout: 图片保存路径
        :param width: 图片修改的宽度
        :param height: 图片修改的高度
        :return: 木有返回值
        '''
        images = self.get_Images()
        if not os.path.exists(self.new_fpath):
            os.mkdir(self.new_fpath)

        for i in range(len(images)):
            filein = self.fpath + images[i]
            fileout = self.new_fpath + str(i) + '.jpg'
            img = Image.open(filein)
            out = img.resize((TARGET_WIDTH, UNIT_SIZE), Image.ANTIALIAS)  # resize image with high-quality
            out.save(fileout)

    def get_Images(self):
        '''获取某文件夹下所有的文件名称
        :param fpath: 图片文件路径
        :return images: 图片文件名
        '''
        images = []
        for root, dirs, files in os.walk(self.new_fpath):  # 遍历文件夹下的所有文件,根文件夹下还有子文件夹，则自上而下遍历
            for f in files:
                images.append(f)
            break  # 当根文件下还有其他的文件夹时，只读取根文件夹下的文件
        return images

    def image_Stitching(self, images, horizontal_num, vertical_num):
        '''横向纵向拼接
        :param images: 图片地址
        :param horizontal_num: 行数
        :param vertical_num: 列数
        :return: 木有返回值
        '''
        target = Image.new('RGB', (TARGET_WIDTH * horizontal_num, UNIT_SIZE * vertical_num))
        for i in range(vertical_num):
            imagefile = []
            for j in range(horizontal_num):
                img = Image.open(self.new_fpath + images[i * horizontal_num + j])
                imagefile.append(img)

            left = 0
            right = TARGET_WIDTH
            for image in imagefile:
                target.paste(image, (left, UNIT_SIZE * i, right, UNIT_SIZE * (i + 1)))  # 将image复制到target的指定位置中
                left += TARGET_WIDTH  # left是左上角的横坐标，依次递增
                right += TARGET_WIDTH  # right是右下的横坐标，依次递增
        quality_value = 100  # quality来指定生成图片的质量，范围是0～100
        target.save(self.photoWall_fpath + 'result' + str(horizontal_num) + str(vertical_num) + '.jpg',
                    quality=quality_value)

    def start(self):

        # 指定爬取一定页数范围内的内容
        for i in range(1, 2):
            url = self.url + '?pn=' + str(i)
            self.dealText(url)
            for purl in self.datas:
                self.saveImg(purl)

        print("图片下载成功，已保存在本地")


    def pilDeal(self):
        print("图片大小修订中.......")
        self.ResizeImage()
        print("图片大小修订完成")

        print("图片拼接中.....")
        print("请输入拼接要求，几行几列")
        horizontal_num = int(input("先输入行数：\n"))
        vertical_num = int(input("再输入列数：\n"))
        images = self.get_Images()

        sums = vertical_num * horizontal_num
        if (sums > len(images)):
            print("输入的行数、列数过大，该文件下没有" + str(sums) + "张图片")
        else:
            self.image_Stitching(images, horizontal_num, vertical_num)
            print("照片拼接成功！")

if __name__ == '__main__':
    pp = BaiduTiebaPhoto()
    #爬取图片保存到本地
    # pp.start()

    #利用Pillow将抓取的图片拼接，形成照片墙
    pp.pilDeal()