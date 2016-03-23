js表格
========

对mmgrid表格插件生成时候的优化,可以有效减少代码量,增加函数的复用

主要涉及到的三个js文件

* js/device/common-validate.js : 主要是数据验证的函数
* js/device/common-mmgrid.js : 主要是表格组件渲染生成相关的函数
* js/device/common-convert.js : 主要是数据转换的函数

其他根据需要自己添加

使用:
--------

1. 构造的列
^^^^^^^^^^^^^^^

根据需要可以将所有需要生成的列放入一个数组中,如下:

.. code-block:: javascript

    var col_items = [
        {title: '头像', render: mmgrid.renderHeaderHtml},
        {title: '帐号', name: 'user_id', render: mmgrid.renderUserDetail},
        {
            title: '帐号类型',
            name: 'user_account_type',
            render: mmgrid.renderHtml,
            convert: CommonConvert.convertAccountType
        },
        {title: '用户类型', name: 'user_type', render: mmgrid.renderHtml, convert: CommonConvert.convertUserType}
    ]

数组中每个对象接收的参数如下:

.. code-block:: javascript

    {
        title: "",
        width: 60,
        align: 'center',
        name: '',
        sortable: false,
        nowrap: false,
        hidden: '',
        // convert接收一个转换函数名
        convert: '',
        // render接收一个函数名
        render: functionName
    }

上面有些参数不需要传递值,是有默认参数的,你也可以传递不同的值将其覆盖.
必须要写的参数是 name, 否则在render中获取不到对应的这一列的值, 就会出错

其中:

* convert: 接收的函数是将在render的函数中使用, 对于有些渲染的返回值需要转换的,这个时候就可以写一个函数传入,如果没有,则直接返回原始值
* render: 这个渲染函数跟mmgrid表格原始的renderer参数对应,但是,我们传入的这个函数是在renderer函数的内部执行的,所得到的结果会返回给renderer,然后由renderer再次返回.这个函数的参数由renderer中传入,会传入三个值: val, item, defaultSetting,从这三个值中可以获取到所有的信息

其他参数基本都与mmgrid中相同

2. 生成表格需要的列
^^^^^^^^^^^^^^^^^^^^

根据第一步中构造的列的信息,生成mmgrid中原本的列的信息,调用一个函数即可:

.. code-block:: javascript

    var cols = mmgrid.generateGridCols(col_items);

这样生成的cols就是和原始的列的信息是一致的,这时候可以将列参数传入构造一个mmgrid对象

3. 渲染表格
^^^^^^^^^^^^^^^

渲染表格的代码和格式如下:

.. code-block:: javascript

    var mmg = mmgrid.renderGrid($('#table6-1'),
        {
            cols: cols,
            url: "/device/user/user",
            method: 'post',
            plugins: [$('#paginator11-1').mmPaginator()],
            params: contactParams
        });

在这里面,第一个参数是表格的id或者class选择器,第二个参数就是表格可以复写的参数字段,原表格中的字段如下:

.. code-block:: javascript

    var defaultSetting = {
        cols: [],
        height: "auto",
        url: '',
        method: 'get',
        remoteSort: true,
        fullWidthRows: true,
        sortName: '',
        sortStatus: 'asc',
        nowrap: true,
        plugins: [],
        params: function () {
            return {};
        }
    };
这里面的参数都是一致的,最后返回一个mmgrid对象

表格生成后还可以绑定一些过滤事件,如下:

.. code-block:: javascript

    mmgrid.filterGrid($("#btnFilter"), mmg);

这个是表格的过滤重新加载的事件绑定,可以自己定义其他的


其他一些函数主要是和表格渲染和数据转换验证相关,可以看那三个文件中是否有,如果已经存在,直接调用即可;没有的话自己写上去,记得写注释!

根据函数功能写在不同的文件中,如果功能不属于这三个,可以自己创建,规范代码,不要有太多警告.

