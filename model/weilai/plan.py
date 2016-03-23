# !/bash/bin/env python
# -*- coding: utf-8 -*-
import datetime
from django.db import models
from model.weilai.user import User

__author__ = 'rdy'


class Plan(models.Model):
    """
    用户表
    """
    # 计划编号
    plan_id = models.AutoField(primary_key=True, db_column='wlf_plan_id')
    # 用户账号
    user_id = models.ForeignKey(User, db_column='wlf_user_id')
    # 计划内容
    plan_msg = models.CharField(max_length=2048, null=True, db_column='wlf_plan_msg')
    # 计划类型(0：日常计划，1：重复计划，2：分享计划，3:分配计划)
    plan_type = models.IntegerField(max_length=2, default=0, db_column='wlf_plan_type')
    # 计划提醒时间
    remind_date = models.DateTimeField(null=True, db_column='wlf_plan_remind_date')
    # 计划是否完成(0:否,1:是)
    is_finish = models.IntegerField(max_length=1, default=0, db_column='wlf_plan_is_finish')
    # 计划创建时间
    create_date = models.DateTimeField(null=True, db_column='wlf_plan_create_date')
    # 计划完成时间
    finish_date = models.DateTimeField(null=True, db_column='wlf_plan_finish_date')

    class Meta:
        app_label = 'home'
        db_table = "wlt_plan"