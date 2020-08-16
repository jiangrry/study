# -*- coding:utf-8 -*-
# author:jiangrry

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # return '我是首页!'
    return '<form method="POST" action="/index2">' \
           '<input type="submit" value="提交">' \
           '</form>'


# @app.route('/post', methods=['POST'])
@app.route('/index2', methods=['POST'])
def index2():
    return '以POST方式请求'


app.run(debug=True)
