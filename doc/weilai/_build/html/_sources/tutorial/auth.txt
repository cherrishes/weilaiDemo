登录会话与权限
=============

登录会话
--------

登录模块封装在一个类中，方便统一管理和维护，同时减少重复代码，在其它视图中直接调用即可


管理员用户登录时可取到的数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # 登录
    OnlineUser(request).login(user)

    # 登出
    OnlineUser(request).logout()

    # 是否已经登录
    OnlineUser(request).is_login()

    # 获取当前登录用户的用户名
    user_name=OnlineUser(request).get_user_name()

    # 获取当前登录用户的用户类型
    user_type=OnlineUser(request).get_user_type()


厂商帐号登录时可取到的数据
^^^^^^^^^^^^^^^^^^^^^^^

::

    # 登录
    FactoryOnlineUser(request).login(user)

    # 登出
    FactoryOnlineUser(request).logout()

    # 是否已经登录
    FactoryOnlineUser(request).is_login()

    # 获取当前登录用户的用户名
    user_name=FactoryOnlineUser(request).get_user_name()

    # 获取当前登录用户的用户类型
    user_type=FactoryOnlineUser(request).get_user_type()

    # 获取当前用户所属厂商编号
    factory_id=FactoryOnlineUser(request).get_factory_id()

    # 获取当前用户所属厂商uid
    factory_uid=FactoryOnlineUser(request).get_factory_uid()


代理商帐号登录时可取到的数据
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # 登录
    AgencyOnlineUser(request).login(user)

    # 登出
    AgencyOnlineUser(request).logout()

    # 是否已经登录
    AgencyOnlineUser(request).is_login()

    # 获取当前登录用户的用户名
    user_name=AgencyOnlineUser(request).get_user_name()

    # 获取当前登录用户的用户类型
    user_type=AgencyOnlineUser(request).get_user_type()

    # 获取当前用户所属厂商编号
    factory_id=AgencyOnlineUser(request).get_factory_id()

    # 获取当前用户所属厂商uid
    factory_uid=AgencyOnlineUser(request).get_factory_uid()

    # 获取当前用户所属代理商编号
    agency_id=AgencyOnlineUser(request).get_agency_id()

    # 获取当前用户所属代理商uid
    agency_uid=AgencyOnlineUser(request).get_agency_uid()
