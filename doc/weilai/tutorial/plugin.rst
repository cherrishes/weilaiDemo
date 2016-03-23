插件开发
========

概述
-------

设备管理系统的插件能做什么？
^^^^^^^^^^^^^^^^^^^^^^^^^

#. 对数据呈现方式的业务逻辑进行个性化的定制（后台的数据筛选、新增数据列，前端界面的展示方式）

插件目录结构
-----------

插件文件夹目录树

::

    .
    └── testplugin     # 插件名称(唯一)
        ├── about.json      # 插件描述文件
        ├── device  # 扩展模块（此处为对“设备管理”进行扩展）
        │   ├── plugin.css # 对前端部分进行扩展的样式
        │   ├── plugin.js # 对前端部分进行扩展的脚本
        │   └── plugin.py # 对后台功能进行扩展的代码
        └── repair # 扩展模块（此处为对“故障报修”进行扩展）
            └── plugin.py

描述文件about.json的格式示例

::

    {
        "name": "testplugin",
        "alias": "测试的插件",
        "version": 1.0,
        "auth": "53iq",
        "description": "这是测试的插件",
        "icon": "http://www.53iq.com/static/img/home/130726logo.png",
        "extension": ["device", "repair"]
    }

plugin.py文件示例

::

    # -*- coding: utf-8 -*-
    import json


    class Plugin():
        def __init__(self):
            pass

        def hook(self, response, request, db_instance):
            if "text/html; charset=utf-8" == response["Content-Type"]:
                ret = response.content.decode("utf-8")
                ret_obj = json.loads(ret)
                ret_obj["totalCount"] = 18
                response.content = json.dumps(ret_obj)
            return response




说明：

#. 插件以zip的方式打包，要添加插件时在插件管理器中上传添加即可


设备管理系统扩展点
-----------------

设备管理页面
^^^^^^^^^^^


