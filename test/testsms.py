# !/bash/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'rdy'
import top.api
from conf.smsconf import APPKEY, APPSECRET
req = top.api.AlibabaAliqinFcSmsNumSendRequest('gw.api.taobao.com/router/rest', 80)
req.set_app_info(top.appinfo(APPKEY, APPSECRET))

req.extend = "123456"
req.sms_type = "normal"
req.sms_free_sign_name = "大鱼测试"
req.sms_param = {'code': '568795', 'product': '微来科技'}
req.rec_num = "15267183467"
req.sms_template_code = "SMS_5920155"
try:
    resp = req.getResponse()
    print(resp, '111')
except Exception as e:
    raise e
    print(e, 'ooo')