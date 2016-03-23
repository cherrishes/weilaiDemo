缓存规范
=========

这里简单的整理规范设备管理系统用到的缓存键值，包括redis和memcached，为大家以后使用或增加新键值提供方便查询，有问题及时反馈谢谢！

memcache键值说明
------------------

.. code-block:: bash

    # 管理员登录session键名,通过以下key可以取到管理员登陆账号
    SESSION_LOGIN
    eg: {'SESSION_LOGIN': 'admin'}

    # 用户登陆账号，通过以下key可以取到一般用户登陆的账号
    SESSION_USER_ID
    eg: {'SESSION_USER_ID': 'xyjadmin'}

    # 厂商编号（数字），通过以下key可以取到厂商的数字编号
    SESSION_FACTORY_ID
    eg: {'SESSION_FACTORY_ID': 3}

    # 厂商唯一标识符，通过以下key可以取到厂商的UUID唯一标识
    SESSION_FACTORY_UID
    eg: {'SESSION_FACTORY_UID': 'ddb4c038-579a-11e5-9e88-00a0d1eb6068'}

    # 代理商编号（数字），通过以下key可以取到代理商数字编号
    SESSION_AGENCY_ID
    eg: {'SESSION_AGENCY_ID': 6}

    # 代理商唯一标识，通过以下key可以取到代理商的UUID唯一标识
    SESSION_AGENCY_UID
    eg: {'SESSION_AGENCY_UID': '9bf4f29e-9d81-11e5-af75-00a0d1edbe70'}

    # 用户类型，通过以下key可以取到登陆系统的用户类型，说明1：管理员，2：厂商，3：代理商
    SESSION_USER_TYPE
    eg: {'SESSION_USER_TYPE': 1}

    # 用户系统皮肤，通过以下key可以取到用户保存的皮肤类型，目前有‘skin-green-dark’，‘skin-black’
    SESSION_SKIN
    eg: {'SESSION_SKIN': 'skin-green-dark'}

    # 用户头像地址，通过以下key可以取到用户保存的头像地址
    SESSION_HEAD_PORTRAIT
    eg: {'SESSION_HEAD_PORTRAIT': 'http://wx.qlogo.cn/mmopen/1J94t9spd9G6icKAPXjsUyeDxJZZV5bhnCIGuxBRlfypicwNicNw80X36caib1YgQVg4bzhDTOnFzBicxpRFWo91ThTt6aVcjXjeib/0'}


安全相关
^^^^^^^^^

.. code-block:: bash

    # 登录次数(失败一次后需要输入验证码)，通过以下key可以取到当前尝试登陆次数
    SESSION_LOGIN_TIME
    eg: {'SESSION_LOGIN_TIME': 1}

    # 短息验证码，通过以下可以取到1分钟内申请的短息验证码
    SESSION_LOGIN_VALIDATE
    eg: {'SESSION_LOGIN_VALIDATE': '356845'}

    # 登录重定向uri，通过以下key可以取到当前重定向的url地址
    SESSION_REDIRECT_URI
    eg: {'SESSION_REDIRECT_URI': '/device'}

    # 发送洗涤命令，通过以下key可以取到最近一次通过后台发送的洗衣机操作命令(有疑问？？？？）
    SESSION_SEND_WASH_CMD
    eg: {'SESSION_SEND_WASH_CMD': ''}


redis键值说明
----------------
设备管理系统使用的库主要是DB2和DB4

.. code-block:: bash

    # 短信验证码前缀，超时时间10分钟，通过以下key可以从redis中取到最近10分钟保存的短息验证码
    sms_check_code_prefix_+{user_id}
    eg: {'sms_check_code_prefix_xyjadmin': '236854'}

    # 通过洗衣机的mac取得对应编号，无超时时间
    mac_prefix_+{C893464254}
    eg: {'mac_prefix_+C893464254' : 'XYJ0000001'}

    # 通过device_id查找factory_uid前缀
    factory_uid_by_device_id_+{device_id}
    eg: {'factory_uid_by_device_id_XYJ0000001': 'cd396786-579a-11e5-9e88-00a0d1eb6068'}

    # 推荐商品版本键，通过以下key可以取到当前准备推荐的商品的版本编号
    kitchen_easy_goods_version
    eg: {'kitchen_easy_goods_version': 123}

    # 送水电话前缀，通过以下key可以取到某台设备绑定的送水电话
    kitchen_easy_telephone_prefix_+{device_id}
    eg: {'kitchen_easy_telephone_prefix_100000215': '15267186539'}

DB2(友联洗衣机项目用到)

.. code-block:: bash

    # 根据设备别名 查 设备编号
    alias_prefix_+{XYJ0000001}
    eg:
    # 键名：alias_prefix_C893464C67B2
    # 键值如下（字符串）：
    {
    "fields": {
        "device_latitude": "45.77322463",
        "device_ip": "218.203.63.168",
        "device_city": "哈尔滨市",
        "device_tag": "",
        "device_type": 1,
        "device_county": "",
        "device_alias": "XYJ0000167",
        "factory_id": 4,
        "device_province": "黑龙江省",
        "device_is_online": 0,
        "device_longitude": "126.65771686",
        "device_model": "",
        "device_property": "{\"wash_mode\": [{\"alias\": \"strong\", \"time\": 3480, \"fee\": 5, \"name\": \"\\u52a0\\u5f3a\\u6d17\"}, {\"alias\": \"standard\", \"time\": 2400, \"fee\": 4, \"name\": \"\\u6807\\u51c6\\u6d17\"}, {\"alias\": \"quick\", \"time\": 1500, \"fee\": 3, \"name\": \"\\u5feb\\u901f\\u6d17\"}, {\"alias\": \"molt\", \"time\": 540, \"fee\": 1, \"name\": \"\\u5355\\u8131\\u6c34\"}]}",
        "protocol_id": 5,
        "device_create_date": "2016-01-12T16:15:38",
        "agency_id": 1,
        "device_mac": "",
        "dt_id": 4,
            "device_address": "黑龙江省哈尔滨市"
        },
        "model": "api.device",
        "pk": "860719024423737"
    }

    # 友联优惠信息配置缓存
    # 键名：uline_discount_setup
    # 键值示例：
    {"DISCOUNT_LAST_DAYS": "30", "DISCOUNT_CONTENT_2": "\uff08\u9996\u6b21\u4f7f\u7528\u4f18\u60e0\u4ef7\uff09", "DISCOUNT_START": "20150222080000",
    "DISCOUNT_CONTENT_1": "\uff08\u5206\u4eab\u670b\u53cb\u5708\u4f18\u60e0\u4ef7\uff09", "DISCOUNT_PRICE": "0.01"}




