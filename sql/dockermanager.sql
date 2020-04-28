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

CREATE TABLE dm_docker_container(
  `id` int(11) AUTO_INCREMENT PRIMARY KEY COMMENT '自增id',
  `docker_id` varchar(32) NOT NULL DEFAULT '' COMMENT 'docker容器id,业务id',
  `project_id` varchar(32) NOT NULL DEFAULT '' COMMENT '项目id，对应表dm_project',
  `container_id` varchar(32) NOT NULL DEFAULT '' COMMENT '对应容器启动后的container_id',
  `git_address` varchar(64) NOT NULL DEFAULT '' COMMENT '拉取对应项目的git地址',
  `git_branch` varchar(32) NOT NULL DEFAULT '' COMMENT '对应项目的git分支',
  `image_name` varchar(32) NOT NULL DEFAULT '' COMMENT '镜像名称',
  `net_name` varchar(32) NOT NULL DEFAULT '' COMMENT '对应网络名称',
  `net_ip` varchar(16) NOT NULL DEFAULT '' COMMENT '对应容器启动的ip地址(内网)',
  `project_creator_id` varchar(32) NOT NULL DEFAULT '' COMMENT '项目创建者用户id',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP  COMMENT '创建日期',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日期',
  UNIQUE KEY `uniq_docker_id` (docker_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT 'docker容器信息表';