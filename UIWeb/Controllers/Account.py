#!/usr/bin/env python
# -*- coding:utf-8 -*-
import io
from Infrastructure import CheckCode
from ..Core.HttpRequest import WebRequestHandler
from Model.User import UserService
from Repository.UserRepository import UserRepository
from UIWeb.Forms.Login import Loginform



class CheckCodeHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        stream = io.BytesIO()
        img, code = CheckCode.create_validate_code()
        img.save(stream, "png")
        self.session["CheckCode"] = code
        self.write(stream.getvalue())


class LoginHandler(WebRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Account/Login.html')

    def post(self, *args, **kwargs):
        form = Loginform()
        form.valid(self)
        print(form._value_dict,
        form._error_dict,
        form._valid_status)
        if form._value_dict:
            if form._value_dict['checkcode'] !=self.session['CheckCode']:
                form._error_dict['checkcode'] = '验证码错误'
        if form._valid_status:
            self.redirect('Pay.html')
        # name = self.get_argument('username')
        # pwd = self.get_argument('pwd')
        # code = self.get_argument('checkcode')
        # ret = UserService(UserRepository())
        # ret = ret .get_user_by_name_pwd(name,pwd)
        # if code.upper() == self.session['CheckCode'].upper():
        #     if ret :
        #         self.session['login']=True
        #         self.redirect('Pay.html')
        # else:
        #     self.render('Account/Login.html')

class LogoutHandler(WebRequestHandler):

    def get(self, *args, **kwargs):

        self.redirect('/Login.html')


class RegisterHandler(WebRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Account/Register.html')










