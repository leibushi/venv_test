# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 14:32
# @Author  : Mqz
# @FileName: hello.py
from flask import Flask

app = Flask(__name__)
@app.route('/index')

def index():
    return 'hello, World'

if __name__ == '__main__':
    app.run()

