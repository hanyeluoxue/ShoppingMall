#!/usr/bin/env python
# -*- coding:utf-8 -*-
from ..Core.HttpRequest import WebRequestHandler
from Model.Category import CategoryService
from Repository.CategoryRepository import CategoryRepository
import json

from Model.Product import ProductService
from Repository.ProductRepository import ProductRepository

from tornado import escape





class IndexHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        # 获取一级分类
        # 循环一级分类，获取二级分类
        # 循环二级分类，获取三级分类
        c = CategoryService(CategoryRepository())
        category_list = c.get_all_category()

        p = ProductService(ProductRepository())
        product_dict = p.fetch_index_product()

        self.render('Home/Index.html', category_list=category_list, product_dict=product_dict)



class DetailHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        price_id = kwargs.get('price_id', None)
        if not product_id or not price_id:
            self.redirect('/Index.html')
            return

        # 根据商品ID获取商品信息，商户信息，价格列表，图片
        p = ProductService(ProductRepository())
        product_dict = p.fetch_product_detail(product_id, price_id)

        self.render('Home/Detail.html', product_dict=product_dict)



class PayHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        try:
            if self.session['login']:
                qqqqq = self.get_cookie('jd_buy_list')
                ret = escape.url_unescape(qqqqq)
                print(ret)
                self.render('Home/Pay.html')
            else:
                self.redirect('Login.html')
        except Exception:
            self.redirect('Login.html')
