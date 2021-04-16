# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 14:37
# @Author  : Mqz
# @FileName: pyautogui_study.py
import pyautogui
import time
w, h = pyautogui.size()

pyautogui.moveTo(w/2, h/2)# 基本移动
#
# pyautogui.moveTo(100,200, duration=2)# 移动过程持续2s完成
#
# pyautogui.moveTo(100, 500)# X方向不变，Y方向移动到500
#
# pyautogui.moveRel(40, 500)# 相对位置移动
# pyautogui.moveTo(40, 1300)# 相对位置移动
# time.sleep(1)
#
# pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"
import pyautogui
import time

# time.sleep(5)  # 5秒种时间切换到画板程序
#
# pyautogui.moveTo(200, 200, duration=1)  # 鼠标移动到(200,200)的位置
#
# pyautogui.dragRel(100, 0, duration=1)
# pyautogui.dragRel(0, 100, duration=1)
# pyautogui.dragRel(-100, 0, duration=1)
# pyautogui.dragRel(0, -100, duration=1)

import pyautogui
from selenium import webdriver
from time import sleep

# dr = webdriver.Chrome()
# def size():
#
#    x=dr.get_window_size()["width"]#获取当前屏幕的宽
#    y=dr.get_window_size()["height"]#获取当前屏幕的高
#    return (x,y)

#左滑
# def left():
#
#    sz=size()
#    x1=int(sz[0]*0.9)
#    x2=int(sz[0]*1.3)
#    y1=int(sz[1]*1.2)
#    pyautogui.click(x1,y1,button='left')
#    pyautogui.mouseDown()
#    pyautogui.moveTo(x2,y1,duration=0.25)
#    pyautogui.mouseUp()
#    sleep(1)
#
# dr.get("https://shopcs.yunyoute.com/login")
# dr.maximize_window()
# sleep(2)
# left()
import random
a1 = random.randint(0,360)
a2 = random.randint(0, 360-a1)
a3 = random.randint(0, 360-a1-a2)
a4 = random.randint(0, 360 - a1-a2-a3)
a5 = 360 -a1 -a2 -a3 -a4
print(a1, a2, a3, a4, a5)