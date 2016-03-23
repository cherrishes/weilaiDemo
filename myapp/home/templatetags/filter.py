from time import strftime, localtime
import datetime

from django import template


register = template.Library()
'''自定义django模板过滤器'''


def dw_get(obj, key):
    """
    解决django中变量不能以下划线开头的问题
    :param obj:
    :param key:
    :return:
    """
    return obj.get(key, '')


register.filter(dw_get)


@register.filter
def wl_convtimespan(obj):
    """
    时间戳字符串转为日期字符串
    001426156087731
    :param obj:
    :return:
    """
    res = ""
    if len(obj) == 15:
        strobj = obj[2:12]
        try:
            res = strftime("%Y-%m-%d %H:%M:%S", localtime(int(strobj)))
        except:
            pass
    return res

register.filter(wl_convtimespan)


@register.filter
def wlutc2local(obj):
    """
    将utc时间转为本地时间
    :param obj:
    :return:
    """
    try:
        date4 = obj + datetime.timedelta(hours=8)
        dtstr = date4.strftime("%m-%d %H:%M")
        return dtstr
    except:
        return ""

register.filter(wlutc2local)

