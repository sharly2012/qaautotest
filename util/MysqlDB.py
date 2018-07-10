#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql


class MysqlDB():
    def connect_db(self):
        # 打开连接数据库
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='test',
                             use_unicode=True,
                             charset="utf8")
        return db

    def query_db(self, name):
        str = ("SELECT * FROM user WHERE username = '%s'" % name)
        con = self.connect_db()
        cur = con.cursor()
        try:
            cur.execute(str)
            rows = cur.fetchall()
            for row in rows:
                id = row[0]
                username = row[1]
                password = row[2]
                age = row[3]
                return id, username, password, age
        except RuntimeError:
            print('找不到数据')
        cur.close()
        con.close()

    def insert_db(self, name, password, age):
        con = self.connect_db()
        cur = con.cursor()
        try:
            str = ("INSERT INTO user(username,password,age) VALUES('%s','%s',%d)" % (name, password, age))
            cur.execute(str)
            con.commit()
            return True
        except RuntimeError:
            con.rollback()
            raise
        finally:
            cur.close()
            con.close()

    def update_db(self, name, age):
        con = self.connect_db()
        cur = con.cursor()
        try:
            str = ("UPDATE user SET age = %d WHERE username = '%s'" % (age, name))
            cur.execute(str)
            con.commit()
            return True
        except RuntimeError:
            con.rollback()
            raise Exception
        finally:
            cur.close()
            con.close()

    def delete_db(self, name):
        con = self.connect_db()
        cur = con.cursor()
        try:
            str = ("DELETE FROM user WHERE username = '%s'" % (name))
            cur.execute(str)
            con.commit()
            return True
        except RuntimeError:
            con.rollback()
            raise Exception
        finally:
            cur.close()
            con.close()


if __name__ == "__main__":
    test = MysqlDB()
