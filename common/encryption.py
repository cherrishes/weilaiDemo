# !/bash/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rdy'
import hashlib


def md5(val):
    """
    字符串MD5加密
    :param val:
    :return:
    """
    if isinstance(val, str):
        m = hashlib.md5()
        m.update(val.encode('utf-8'))
        return m.hexdigest()
    else:
        return ''


if __name__ == '__main__':
    r = md5('123')
    print(r)