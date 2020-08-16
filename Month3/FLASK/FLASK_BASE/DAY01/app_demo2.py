# -*- coding:utf-8 -*-
# author:jiangrry
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "<h1>这是首页</h1>"


@app.route('/admin/login/form/show/<name>')
def show(name):
    return "参数的值为:%s" % name


@app.route('/url')
def url():
    # 通过index()解析出对应的访问路径
    url_index = url_for('index')
    print("index():" + url_index)
    # 通过show(name)解析出对应的访问路径
    url_show = url_for('show', name='wangwc')
    print("show(name):" + url_show)
    return "<a href='%s'>访问show(name)</a>" % url_show


if __name__ == "__main__":
    app.run(debug=True)

