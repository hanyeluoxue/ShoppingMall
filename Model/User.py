#!/usr/bin/env python
# -*- coding:utf-8 -*-

class IUserRepository:

    pass


class UserService:

    def __init__(self, user_repository):
        self.userRepository = user_repository

    def get_user_to_select(self):

        user_list = self.userRepository.fetch_user()

        return user_list

    def get_user_by_name_pwd(self,name,pwd):

        user = self.userRepository.fetch_one_user_by_name_pwd(name,pwd)
        return user