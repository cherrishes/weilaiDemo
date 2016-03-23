# !/bash/bin/env python
# -*- coding: utf-8 -*-
import datetime
from django.db import models

__author__ = 'rdy'


class User(models.Model):
    """
    用户表
    """
    # 账号
    user_id = models.CharField(primary_key=True, max_length=128, db_column='wlf_user_id')
    # 内部账号(用于第三方账号登录时关联)
    user_account = models.CharField(max_length=128, null=True, db_column='wlf_user_account')
    # 密码
    user_password = models.CharField(max_length=512, db_column='wlf_user_password')
    # 头像地址
    user_head_url = models.CharField(max_length=1024, null=True, db_column='wlf_user_headurl')
    # 昵称
    user_nickname = models.CharField(max_length=32, null=True, db_column='wlf_user_nickname')
    # 性别(1:男,2:女,0:未知)
    user_gender = models.IntegerField(max_length=1, default=0, db_column='wlf_user_gender')
    # 用户类型（0：普通用户，1：管理员，2：厂商，3：运营商）
    user_type = models.IntegerField(max_length=2, default=0, db_column='wlf_user_type')
    # 账号类型（0：内部账号，1：qq，2：微信，3：新浪微博）
    user_account_type = models.IntegerField(max_length=2, default=0, db_column='wlf_user_account_type')
    # 最近登录时间
    user_login_date = models.DateTimeField(null=True, db_column='wlf_user_login_date')
    # 是否在线（0：离线，1：在线）
    user_is_online = models.IntegerField(max_length=1, default=0, db_column='wlf_user_is_online')
    # 备注
    user_remarks = models.TextField(null=True, db_column='wlf_user_remarks')
    # 创建时间
    user_create_date = models.DateTimeField(default=datetime.datetime.utcnow(), db_column='wlf_user_create_date')
    # 用户关联号码
    user_phone = models.CharField(max_length=32, null=True, db_column='wlf_user_phone')
    # 是否禁用（0：未禁用，1：禁用）
    user_is_forbid = models.BooleanField(default=False, db_column='wlf_user_is_forbid')

    class Meta:
        app_label = 'home'
        db_table = "wlt_user"