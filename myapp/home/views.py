# !/bash/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging
from conf.sessionconf import SESSION_USER_ID

__author__ = 'rdy'
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
            u = User.objects.filter(user_account=user_name, user_password=password)[0]
            if u:
                request.session[SESSION_USER_ID] = user_name
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


@csrf_exempt
def home(request):
    """
    首页
    :param request:
    :return:
    """
    p = Plan.objects.filter(user_id=1).order_by("-create_date")
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
    user_id = 1
    if flag == 'update':
        # 更新状态
        try:
            p = Plan.objects.filter(plan_id=int(plan_num), user_id=user_id)[0]
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
            p.save()
        except Exception as e:
            logging.getLogger('').info('添加任务至数据库出错'+str(e))
            print(e)
    return HttpResponse('ok')