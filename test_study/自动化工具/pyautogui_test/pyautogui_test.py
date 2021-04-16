# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 16:47
# @Author  : Mqz
# @FileName: pyautogui_test.py
import time

import pyautogui
width, height = pyautogui.size() # 屏幕的宽度和高度
print("屏幕宽度", width, height)
currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
print(currentMouseX, currentMouseY)

# 控制鼠标移动,duration为持续时间
# for i in range(2):
#     pyautogui.moveTo(100, 100, duration=0.25)  # 移动到 (100,100) 持续时间0.25秒
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(1):
#     pyautogui.moveRel(50, 0, duration=0.25)  # 从当前位置右移50像素
#     currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
#     print(currentMouseX, currentMouseY)
#
#     pyautogui.moveRel(0, 50, duration=0.25)  # 向下
#     currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
#     print(currentMouseX, currentMouseY)
#
#     pyautogui.moveRel(-50, 0, duration=0.25)  # 向左
#     currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
#     print(currentMouseX, currentMouseY)
#
#     pyautogui.moveRel(0, -50, duration=0.25)  # 向上
#     currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
#     print(currentMouseX, currentMouseY)
#
#
def slide():

    """mouse 模拟滑动"""
    for i in range(2):
        pyautogui.moveRel(50, -25, duration=0.25)  # 从当前位置右移50像素 向上25
        pyautogui.moveRel(50, 25, duration=0.25)  # 从当前位置右移50像素
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

        pyautogui.moveRel(0, 50, duration=0.25)  # 向下
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

        pyautogui.moveRel(-50, -25, duration=0.25)  # 向左
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

        pyautogui.moveRel(0, -50, duration=0.25)  # 向上
        currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
        print(currentMouseX, currentMouseY)

        pyautogui.moveRel(50, 25, duration=0.25)  # 向上

# 按住鼠标左键，把鼠标拖拽到(100, 200)位置
time.sleep(2)

pyautogui.dragTo(100, 200, button='left')
time.sleep(2)
pyautogui.dragTo(300, 200, 2, button='left')
time.sleep(2)
pyautogui.dragTo(500, 200,2, button='left')
# 按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
# pyautogui.dragTo(300, 400, 2, button='left')
# # 按住鼠标左键，用0.2秒钟把鼠标向上拖拽
# pyautogui.dragRel(0, -60, duration=0.2)