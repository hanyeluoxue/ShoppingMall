
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Infrastructure.Form.Forms import BaseForm
from Infrastructure.Form.Fields import StringField


class Loginform(BaseForm):
    def __init__(self):
        self.username = StringField()
        self.pwd = StringField()
        self.checkcode = StringField()

        super(Loginform, self).__init__()