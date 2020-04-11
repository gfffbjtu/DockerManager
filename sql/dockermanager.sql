CREATE TABLE dm_project(
  `id` int(11) AUTO_INCREMENT PRIMARY KEY COMMENT '自增id',
  `project_id` varchar(32) NOT NULL DEFAULT '' COMMENT '项目id',
  `project_name` varchar(32) NOT NULL DEFAULT '' COMMENT '项目名称',
  `project_description` varchar(64) NOT NULL DEFAULT '' COMMENT '项目描述',
  `project_creator_id` varchar(32) NOT NULL DEFAULT '' COMMENT '项目创建者用户id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP  COMMENT '创建日期',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日期',
  UNIQUE KEY `uniq_project_id` (project_id),
  UNIQUE KEY `uniq_project_name` (project_name)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='项目信息表 一个项目下可以有多个Docker，但都在同一网络下';