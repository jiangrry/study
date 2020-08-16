# -*- coding: UTF-8 -*- 
# author(作者):jiangrry
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    # app运行falsk的应用(启动flask的服务),默认在本机开启的端口是5000,port = 5555,
    # 在制定端口启动程序端
    # debug = True 将启动模式更改为调试模式(开发环境中推荐写Ture,生产环境中必须改为False)
    app.run(debug=True)
