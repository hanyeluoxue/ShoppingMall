#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .BaseSession import BaseSession


class MemcacheSession(BaseSession):

    def initialize(self, handler, expires):
        pass