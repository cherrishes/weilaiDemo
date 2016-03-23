环境配置
=========

安装项目
-------

创建虚拟环境
^^^^^^^^^^^

::

    # 安装python版本
    pyenv install 3.4.1
    pyenv global 3.4.1
    # 创建虚拟环境
    pyenv virtualenv 3.4.1 smartsysenv

安装依赖
^^^^^^^^^^^

.. code-block:: bash

    # "requirements.txt"这个文件在源码的根目录下,先删掉“AxmlParserPY==0.1”、“httpheader==1.1”、“python-memcached==1.44”这3行
    pip install -r requirements.txt

    # "python-memcached"、"AxmlParserPY"、"httpheader"这3个依赖包从以下地址下载：
    http://192.168.0.62/file/python3/python-memcached-1.44-mod.zip
    http://192.168.0.62/file/python3/AxmlParserPY-0.01.zip
    http://192.168.0.62/file/python3/httpheader-1.1-py3bug%e4%bf%ae%e5%a4%8d%e7%89%88.zip


    # 解决"Python: The _imagingft C module is not installed"
    # 有些系统，比如ubuntu会报此类错误（centos貌似不会）
    # 安装jpeg库
    wget http://www.ijg.org/files/jpegsrc.v7.tar.gz
    tar -zxvf jpegsrc.v7.tar.gz
    cd jpeg-7
    CC="gcc -arch x86_64"
    ./configure --enable-shared --enable-static
    make && make install

    # 安装相关依赖
    sudo apt-get install libfreetype6-dev
    sudo apt-get install libjpeg-dev
    # 卸载后重新安装
    pip uninstall Pillow
    pip install Pillow==2.8.1

    # 将字体文件复制到系统系统目录中
    wget http://192.168.0.62/file/python3/msyh.ttf
    sudo cp msyh.ttf /usr/share/fonts/
    # 然后重新启动一下项目即可

运行
^^^^

#. 在pycharm中配置好Interpreter,菜单栏--> File --> Settings... --> Project:smartsys --> 选择创建好的虚拟环境
#. 运行，pycharm的右上角有运行按钮，点击后即可运行（或者直接在根目录下执行命令运行：python manage.py runserver 127.0.0.1:8000）
#. 在浏览器中输入：http://127.0.0.1:8000 即可打开设备管理系统站点