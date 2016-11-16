#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Model.User import IUserRepository
from Repository.DbConnection import DbConnection

class UserRepository(IUserRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_user(self):
        cursor = self.db_conn.connect()
        sql = """select nid as value,username as text from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_one_user_by_name_pwd(self,name,pwd):
        cursor = self.db_conn.connect()
        sql = """select nid from userinfo WHERE username=%s and password=%s"""
        cursor.execute(sql,(name,pwd))
        db_result = cursor.fetchone()
        print(db_result)
        self.db_conn.close()
        return db_result