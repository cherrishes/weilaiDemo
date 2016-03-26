
from django.http.response import HttpResponseRedirect

from conf.sessionconf import SESSION_USER_ID


def login_required(func):
    """
    登录装饰器，用于判断是否登录
    设备管理系统登录验证
    :param func:
    :return:
    """
    def wrap(request, **kwargs):
        is_login = SESSION_USER_ID in request.session
        # 登录成功后重定向到请求的uri
        request_uri = request.META.get("PATH_INFO", "/home")

        if not is_login:
            from django.core.urlresolvers import reverse
            return HttpResponseRedirect(reverse("login") + "?uri=" + request_uri)
        else:
            if request_uri:
                return func(request, **kwargs)
            from django.core.urlresolvers import reverse
            return HttpResponseRedirect(reverse("login"))

    return wrap