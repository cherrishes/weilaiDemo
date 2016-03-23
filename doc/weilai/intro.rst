项目介绍
===============

主要模块
------

#. 网站（电脑版、手机版）
#. 管理后台
#. 设备管理系统


目录结构
-------

:: 

    smartsys
    ├── app
    │   ├── device --设备管理系统
    │   │   ├── account --账户模块
    │   │   ├── device --设备模块
    │   │   ├── mall --商城模块
    │   │   ├── statistics --统计模块
    │   │   ├── templatetags
    │   │   └── user --用户模块
    │   ├── home --网站
    │   ├── manage --后台管理
    │  
    ├── cache
    ├── common --公用部分代码
    ├── conf --配置目录(存放配置信息)
    ├── core --装饰器、中间件、插件管理器等核心代码
    ├── demo --示例代码
    ├── doc --文档目录
    │   ├── flowchart
    │   ├── mysql
    │   ├── smartsys
    │   │   ├── _build
    │   │   ├── db
    │   │   ├── _static
    │   │   └── _templates
    │   ├── ui
    │   └── xmind
    ├── example
    ├── extension --插件扩展
    ├── log --日志记录
    ├── model --数据模型
    │   └── device
    ├── smartsys
    ├── static --静态资源
    │   ├── admin
    │   │   ├── css
    │   │   ├── img
    │   │   └── js
    │   ├── arttemplate
    │   ├── bootstrap
    │   │   ├── AdminLTE
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── js
    │   │   └── switch
    │   ├── css
    │   │   ├── device
    │   │   ├── fonts
    │   │   ├── home
    │   │   ├── manage
    │   │   └── wiki
    │   ├── file
    │   ├── font-awesome-4.4.0
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── less
    │   │   └── scss
    │   ├── highcharts
    │   │   ├── adapters
    │   │   ├── modules
    │   │   └── themes
    │   ├── img
    │   │   ├── device
    │   │   ├── head
    │   │   ├── home
    │   │   ├── manage
    │   │   ├── wash
    │   │   └── wiki
    │   ├── js
    │   │   ├── device
    │   │   ├── home
    │   │   ├── manage
    │   │   └── wiki
    │   ├── mmGrid
    │   │   ├── img
    │   │   └── theme
    │   ├── orbited
    │   └── uikit-2.17.0
    │       ├── css
    │       ├── fonts
    │       └── js
    ├── template --模板目录
    │   ├── admin
    │   │   ├── auth
    │   │   ├── edit_inline
    │   │   └── includes
    │   ├── device
    │   │   ├── account
    │   │   ├── device
    │   │   ├── mall
    │   │   ├── statistics
    │   │   └── user
    │   ├── home
    │   ├── manage
    │   └── wiki
    ├── test --单元测试
    ├── tmp  -- 临时文件（里面的内容随意删除）
    └── util --常用工具类封装
        ├── compressor -- 静态资源压缩
        ├── java
        └── sms -- 短信通知
