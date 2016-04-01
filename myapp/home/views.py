# !/bash/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rdy'

import random
import uuid
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging
from common.encryption import md5
from conf.commonconf import IMG_DICT
from conf.sessionconf import SESSION_USER_ID, SESSION_USER_NAME, SESSION_HEAD_PORTRAIT
from core.decorators import login_required

from django.http.response import HttpResponse, HttpResponseRedirect
from model.weilai.user import User
from model.weilai.plan import Plan


def first(request):
    return render(request, 'home/first.html', locals())


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        password = request.POST.get('password', '')
        try:
            u = User.objects.filter(user_account=user_name, user_password=md5(password))[0]
            if u:
                request.session[SESSION_USER_ID] = u.user_id
                request.session[SESSION_USER_NAME] = u.user_nickname
                request.session[SESSION_HEAD_PORTRAIT] = u.user_head_url
                return HttpResponseRedirect('/home')
            else:
                msg = "<div class='ui-error-box' ><b></b><p>用户名或密码错误</P></div>"
                return render(request, 'home/login.html', locals())

        except Exception as e:
            print(e)
            logging.getLogger('').info('')
        msg = "<div class='ui-error-box' ><b></b><p>用户名或密码错误</P></div>"
        return render(request, 'home/login.html', locals())
    user_id = request.session.get(SESSION_USER_ID)
    if user_id:
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'home/login.html', locals())


def logout(request):
    """
    退出登陆
    :param request:
    :return:
    """
    if SESSION_USER_ID in request.session:
        del request.session[SESSION_USER_ID]
    return HttpResponseRedirect(reverse("login"))


@csrf_exempt
def signup(request):
    """
    注册页面
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_name = request.POST.get('user-name', '')
        user_email = request.POST.get('user-email', '')
        user_password = request.POST.get('user-password', '')
        try:
            u = User()
            u.user_id = uuid.uuid4()
            u.user_account = user_email
            u.user_nickname = user_name
            u.user_password = md5(user_password)
            u.user_head_url = IMG_DICT[random.randint(1, 13)]
            u.save()
            suc_msg = "<div class='ui-success-box' ><b></b><p>注册成功，请登陆</P></div>"
            return render(request, 'home/login.html', {'suc_msg': suc_msg})
        except Exception as e:
            print(e)
    return render(request, 'home/signup.html', locals())


@csrf_exempt
@login_required
def home(request):
    """
    首页
    :param request:
    :return:
    """
    user_id = request.session.get(SESSION_USER_ID)
    p = Plan.objects.filter(user_id=user_id).order_by("-create_date")
    finish_plan = []
    un_finish_plan = []
    for i in p:
        if i.is_finish == 0:
            un_finish_plan.append(i)
        else:
            finish_plan.append(i)
    finish_len = len(finish_plan)
    un_finish_len = len(un_finish_plan)
    return render(request, 'home/index.html', locals())


def fun(request):
    """
    娱乐
    :param request:
    :return:
    """
    return render(request, 'home/found.html', locals())


def week_list(request):
    """
    周排行榜
    :param request:
    :return:
    """
    return render(request, 'home/week_list.html', locals())


def chat(request):
    """
    聊天交友
    :param request:
    :return:
    """
    return render(request, 'home/chat.html', locals())


@csrf_exempt
@login_required
def deal_plan(request):
    """
    处理任务状态
    :param request:
    :return:
    """

    plan_num = request.POST.get('plan_num', '-1')
    flag = request.POST.get('flag', '')
    msg = request.POST.get('msg', '')
    # 后期这个user_id直接从缓存中取
    user_id = request.session.get(SESSION_USER_ID)
    if flag == 'update':
        # 更新状态
        try:
            p = Plan.objects.filter(user_plan_id=int(plan_num), user_id=user_id)[0]
            if p:
                p.is_finish = 1
                p.finish_date = datetime.datetime.utcnow()
                p.save()
        except Exception as e:
            logging.getLogger('').info('更新任务状态出错'+str(e))
            print(e)
        return HttpResponse('ok')
    elif flag == 'add':
        # 增加任务
        try:
            p = Plan()
            p.plan_msg = msg
            p.create_date = datetime.datetime.utcnow()
            p.user_id = User.objects.get(user_id=user_id)
            p.user_plan_id = int(plan_num)
            p.save()
        except Exception as e:
            logging.getLogger('').info('添加任务至数据库出错'+str(e))
            print(e)
    return HttpResponse('ok')


@csrf_exempt
@login_required
def detail(request):
    """
    任务详情
    :param request:
    :return:
    """
    plan_id = request.GET.get('plan_id', '')
    try:
        p = Plan.objects.get(plan_id=plan_id)
    except Exception as e:
        print(e)
    return render(request, 'home/detail.html', locals())