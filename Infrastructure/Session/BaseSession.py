#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Config import SESSION_EXPIRES
import os
import time
from hashlib import sha1


class BaseSession:
    def __init__(self, handler):
        self.handler = None
        self.random_str = None
        self.initialize(handler, expires = SESSION_EXPIRES)

    session_id = "__sessionId__"

    create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()

