详情页面
========

设备详情
--------

* 通过统一的中转页面进行权限控制和具体的页面跳转
* 在需要跳转到详情页的链接中拼接上设备编号或者设备别名即可

使用示例
::

    <a href="/device/device/detail/C893464C67B2">进入设备详细页面</a>
    # 或者
    <a href="{% url "device_detail" "XYJ0000001" %}">进入设备详细页面</a>

订单详情
--------

* 主要用于订单相关页面，点击订单号后跳转的详情页面

使用示例
::

    <a href="/device/account/order_detail/14513116900375473">进入订单详细页面</a>

用户详情
--------

* 主要用于用户相关页面，点击用户id后跳转的详情页面

使用示例
::

    <a href="/device/user/user_detail/2_o3rSQwxqIkYug8hQaMr4lU-_gt7U">进入用户详请页面</a>
