# -*- coding: utf-8 -*-
# @Time    : 2020/4.txt/23 18:13
# @Author  : Mqz
# @FileName: 5.txt.i_o.py
import re

# 你不用太关心这个函数
def parse(text):
#  使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', ' ', text)
    # print(text)
    # 转为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    print(word_list)
    # 去除空白单词
    word_list = filter(None, word_list)
    # print(word_list)
    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        # print(word)
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # print(word_cnt)
    #  按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

            # sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1.txt], reverse=True)
    return sorted_word_cnt
with open('in', 'r') as fin:
    text = fin.read()
    # word_and_freq = parse(text)

word_and_freq = parse(text)
# print(word_and_freq)
#
with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))



# 好，回到我们的话题。在拿到指针后，我们可以通过 read() 函数，来读取文件的全部内容。代码 text = fin.read() ，即表示把文件所有内容读取到内存中，并赋值给变量 text。这么做自然也是有利有弊：优点是方便，接下来我们可以很方便地调用 parse 函数进行分析；缺点是如果文件过大，一次性读取可能造成内存崩溃。这时，我们可以给 read 指定参数 size ，用来表示读取的最大长度。还可以通过 readline() 函数，
# 每次读取一行，这种做法常用于数据挖掘（Data Mining）中的数据清洗，在写一些小的程序时非常轻便。如果每行之间没有关联，这种做法也可以降低内存的压力。而