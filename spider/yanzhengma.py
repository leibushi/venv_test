# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 10:16
# @Author  : Mqz
# @FileName: yanzhengma.py

# coding=utf-8🔥

# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2019-5-13
@author: 北京-宏哥   QQ交流群：705269076
Project: What？废柴， 模拟登陆，代码控制滑动验证真的很难吗？Are you kidding？？？
'''

# 3.导入模块
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = '博客园的username'
PASSWORD = '博客园的password'
BORDER = 6

class CrackGeetest():
    def __init__(self):
        self.url = 'https://passport.cnblogs.com/user/signin'
        self.url = 'https://passport.cnblogs.com/user/signin'
        self.browser = webdriver.Chrome()
        # self.browser.maximize_window()  # 将Chrome窗口放大
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def get_login_button(self):
        """
        获取登录按钮，调出极验验证码
        :return: 登录按钮对象
        """
        #button_login = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button')))
        button_login = self.wait.until(EC.element_to_be_clickable((By.ID, 'submitBtn')))
        return button_login

    def get_geetest_button(self):
        """
        获取初始验证按钮，即点击按钮进行验证
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return button

    def get_position(self, flag):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        fullbg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "geetest_canvas_fullbg")))
        time.sleep(2)

        if flag:
            self.browser.execute_script(
                "arguments[0].setAttribute(arguments[1], arguments[2])", fullbg, "style", "")
            print("获取不带缺口的图片成功")
        else:
            self.browser.execute_script(
                "arguments[0].setAttribute(arguments[1], arguments[2])", fullbg, "style", "display: none")
            print("获取带缺口的图片成功")

        location = img.location     # 图像位置
        size = img.size             # 图像大小
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right, size)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_geetest_image(self, flag, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right, size= self.get_position(flag)
        print('验证码位置', top, bottom, left, right, size)
        screenshot = self.get_screenshot()
        # 根据验证码图像位置获取验证码图像
        captcha = screenshot.crop((left, top, right,bottom))
        #captcha.save(name)
        return captcha

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'LoginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'Password')))
        username.send_keys(self.username)
        password.send_keys(self.password)

    def get_gap(self, image1, image2):
        """
        获取带缺口的偏移量
        :param image1: 不带缺口的图片
        :param image2: 带缺口的图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    # left = i
                    # return left
                    return i
        return left

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x,y]
        pixel2 = image2.load()[x,y]
        #print("piexl1", pixel1, "piexl2", pixel2)
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
            #print("True")
            return True
        else:
            #print("False")
            return False

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + a * t
            v = v0 + a * t
            # 移动距离 x = v0*t + 1/2 * a * t^2
            move = v0 * t + 0.5 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def login(self):
        """
        登录
        :return: None
        """
        # submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'submitBtn')))
        # submit.click()
        # time.sleep(10)
        print('登录成功')

    def crack(self):
        # 输入用户名和密码
        self.open()
        # 点击登录按钮，调出验证按钮
        login_button = self.get_login_button()
        login_button.click()

        # 获取验证码图片,不带缺口
        image1 = self.get_geetest_image(True, 'captcha1.png')
        # 点按呼出缺口图片，获取滑块
        slider = self.get_slider()
        # slider.click()    # 现在不需要点击滑块即可呼出缺口图片
        # 获取带缺口的验证码图片
        image2 = self.get_geetest_image(False, 'captcha2.png')

        # 获取缺口位置
        gap = self.get_gap(image1, image2)
        print('缺口位置', gap)

        # 减去缺口位移
        gap -= BORDER

        # 获取移动轨迹
        track = self.get_track(gap)
        print('滑动轨迹', track)

        # 拖动滑块
        self.move_to_gap(slider, track)

        try:
            success = self.wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_panel_success_title'), '通过验证'))
            print(success)
            #self.login()
        except Exception:
            self.crack()

        if success:
            print(success)
            self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()