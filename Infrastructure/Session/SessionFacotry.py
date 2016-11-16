#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Config import SESSION_TYPE
from .CacheSession import CacheSession
from .MemcacheSession import MemcacheSession
from .RedisSession import RedisSession



class SessionFactory:

    __session = None

    @staticmethod
    def get_session(handler):
        if SESSION_TYPE == 'CacheSession':
            session = CacheSession(handler)
        if SESSION_TYPE == 'CacheSession':
            session = MemcacheSession(handler)
        if SESSION_TYPE == 'RedisSession':
            session = RedisSession(handler)
        else:
            session = CacheSession(handler)
        SessionFactory.set_session(session)
        return SessionFactory.__session


    @staticmethod
    def set_session(session):
        SessionFactory.__session = session
