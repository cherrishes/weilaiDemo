项目规范
=======

前端
----

代码
^^^^

#. 标签id的命名采用匈牙利命名法，比如 <input type="button" id="btnSave" value="保存"/>
#. 样式的class以用途和效果来命名，比如：ui-box-content、ui-form-item-focus，具体可以参考支付宝通用样式库： http://aliceui.org/docs/widget.html

浏览器兼容
^^^^^^^^^^

#. 内部使用的可以只支持高版本的浏览器
#. 给用户使用的一般的系统，功能上必须支持IE8+;在不影响使用的情况下，样式上可以适当放松兼容性
#. 主要的展示类网站（比如官网），功能和样式都必须兼容IE8+、firefox最新版、chrome最新版
#. PC版网站分辨率的兼容：1920*1080、1366*768、1440*900、1024*768、1600*900（http://tongji.baidu.com/data/screen）
#. 移动版只需支持ios、android的主流版本的浏览器即可

python
-------

#. 代码书写规范遵循PEP8
#. 遵循DRY (Don't Repeat Yourself) 原则，不要写重复的代码，相同的代码应该抽象出来
#. 虚拟环境名称:smartsysenv

django
------

#. 视图名称与模板文件名称一致，url也尽量与视图名一致,比如配置了个url叫“login”，views.py中的视图叫“login”,模板文件叫“login.html”
#. 所有的静态资源都放在/static/目录下，所有的模板文件都放在/template/目录下


布局
----

#. 分页全部放到内容底部


其它
----

#. 不要在代码里将数据库的连接信息、缓存连接信息等写死，要保存在配置文件中
#. 所有的配置文件都必须保存在 /conf/目录下，包括session、cookie、cache
#. 修改文件前一定要先更新svn，提交之前先更新
#. 不要重复造轮子，有现成的框架就用现成的