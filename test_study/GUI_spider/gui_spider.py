# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 16:02
# @Author  : Mqz
# @FileName: gui_spider.py
import tkinter
#创建界面
root = Tk()
#标题
root.title("网易云音乐下载器")
#窗口大小
root.geometry('550x400')

#标签控件
label = Label(root,text='请输入歌曲名称：',font=("华文行楷",20))
#标签定位
label.grid()

#输入框
entry = Entry(root,font=("隶书",20))
entry.grid(row=0,column=1)

#列表框
text = Listbox(root,font=("楷书",16),width=50,heigh=15)
text.grid(row=1,columnspan=2)

#开始按钮
button = Button(root,text="开始下载",font=("隶书",15))
button.grid(row=2,column=0,sticky=W)

#退出按钮
button1 = Button(root,text="退出程序",font=("隶书",15))
button1.grid(row=2,column=1,sticky=E)

#显示界面
root.mainloop()
# ://blog.csdn.net/weixin_43870646/article/details/104609873————————————————
# # 版权声明：本文为CSDN博主「成都—爬虫工程师—杨洋」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# # 原文链接：https