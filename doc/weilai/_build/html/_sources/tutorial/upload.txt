文件上传
=========

说明
-----

#. 设备管理系统不保存任何用户上传的文件，所有用户上传的文件都保存到云存储中


示例
-----

在模板中通过ajax上传到云存储
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: html

    <input id="form-file" name="eg_thumbnail" type="file"/>
    <script src="{% static 'js/common.min.js' %}"></script>
    <script>
            var upload_file = "{% url 'upload_file' %}";
             $.ajaxFileUpload({
                        url: upload_file + "?ts=" + new Date().getTime(),
                        fileElementId: 'form-file',
                        dataType: 'text',
                        success: function (res, status) {
                            if (status === "success" && /.*\.[(jpg)|(png)|(jpeg)|(bmp)|(gif)]+$/gi.test(res)) {
                                alert(res);
                            } else {
                                alert('图片上传失败');
                            }
                        },
                        error: function (data, status, e) {
                            //服务器响应失败处理函数
                            alert('服务器错误');
                        }
                    });
    </script>