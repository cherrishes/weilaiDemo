mysql
===============

基本信息
--------

* 主机：localhost
* 端口：3306
* 用户：root
* 密码：111111
* 数据库：ebdb_weilai


表结构
-------

.. code-block:: sql

    -- ----------------------------
    -- Table structure for wlt_user
    -- ----------------------------
    DROP TABLE IF EXISTS `wlt_user`;
    CREATE TABLE `wlt_user` (
      `wlf_user_id` varchar(128) NOT NULL COMMENT '账号',
      `wlf_user_account` varchar(128) DEFAULT NULL COMMENT '内部账号(用于第三方账号登录时关联)',
      `wlf_user_password` varchar(512) NOT NULL COMMENT '密码',
      `wlf_user_headurl` varchar(1024) DEFAULT NULL COMMENT '头像地址',
      `wlf_user_nickname` varchar(32) DEFAULT NULL COMMENT '昵称',
      `wlf_user_gender` int(1) NOT NULL DEFAULT '0' COMMENT '性别(1:男,2:女,0:未知)',
      `wlf_user_type` int(2) NOT NULL DEFAULT '0' COMMENT '用户类型（0：普通用户，1：管理员）',
      `wlf_user_account_type` int(2) NOT NULL DEFAULT '0' COMMENT '账号类型（0：内部注册账号，1：qq，2：微信，3：新浪微博）',
      `wlf_user_login_date` datetime DEFAULT NULL COMMENT '最近登录时间',
      `wlf_user_is_online` int(1) NOT NULL DEFAULT '0' COMMENT '是否在线（0：离线，1：在线）',
      `wlf_user_remarks` varchar(64) DEFAULT NULL COMMENT '备注',
      `wlf_user_create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
      `wlf_user_phone` varchar(32) DEFAULT NULL COMMENT '联系电话',
      `wlf_user_is_forbid` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否禁用（0：未禁用，1：禁用）',
      PRIMARY KEY (`wlf_user_id`),
      KEY `Index_1` (`wlf_user_type`),
      KEY `Index_2` (`wlf_user_account_type`)
    ) ENGINE=Innodb DEFAULT CHARSET=utf8 COMMENT='用户表';

    -- ----------------------------
    -- Table structure for wlt_plan
    -- ----------------------------
    DROP TABLE IF EXISTS `wlt_plan`;
    CREATE TABLE `wlt_plan`(
      `wlf_plan_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '计划编号',
      'wlf_user_plan_id' int(11) NOT NULL DEFAULT '0' COMMENT '用户计划编号',
      `wlf_user_id` varchar(128) DEFAULT NULL COMMENT '用户账号',
      `wlf_plan_msg` varchar(2048) DEFAULT NULL COMMENT '计划内容',
      `wlf_plan_type` int(2) NOT NULL DEFAULT '0' COMMENT '计划类型(0：日常计划，1：重复计划，2：分享计划，3:分配计划)',
      `wlf_plan_remind_date` datetime DEFAULT NULL COMMENT '计划提醒时间',
      `wlf_plan_is_finish` int(1) NOT NULL DEFAULT '0' COMMENT '计划是否完成(0:否,1:是)',
      `wlf_plan_create_date` datetime DEFAULT NULL COMMENT '计划创建时间',
      `wlf_plan_finish_date` datetime DEFAULT NULL COMMENT '计划完成时间',
      PRIMARY KEY (`wlf_plan_id`),
      KEY `FK_Reference_1` (`wlf_user_id`),
      CONSTRAINT `FK_Reference_1` FOREIGN KEY (`wlf_user_id`) REFERENCES `wlt_user` (`wlf_user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE=Innodb DEFAULT CHARSET=utf8 COMMENT='计划表';