"""
    编写一个类完成注册和登录
        编写一个类，实例化对象时可以连接数据库
        通过该对象调用方法可以模拟完成简单的登录注册功能。
"""
import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='student',
                                  charset='utf8')
        self.cur = self.db.cursor()

    def close(self):
        """
            關閉　遊標和數據庫對象
        """
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        """
            註冊用戶
        :param name: 用戶名稱
        :param passwd: 用戶密碼
        :return bool 類型　True 註冊成功　False 用戶已存在; 註冊失敗
        """
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False
        sql = "insert into user(name, passwd) values(%s, %s);"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self, name, passwd):
        """
            登錄
        :param name: 用戶名稱
        :param passwd: 用戶密碼
        :return: bool 類型　True 登錄成功　False 登錄失敗
        """
        sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
        self.cur.execute(sql)
        res = self.cur.fetchone()
        if res:
            return True
        else:
            return False


if __name__ == '__main__':
    db = Database()  # 實例化對象　
    register_status = db.register('Tom1', '123456')
    print(register_status)
    login_status = db.login('Tom1', '1234567')
    print(login_status)
    db.close()
