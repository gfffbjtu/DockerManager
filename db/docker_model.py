"""docker数据库操作类"""
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from db.base_model import db, _BaseModel
from common_tool import gen_unique_id
from flask import current_app


class ModelDockerContainer(db.Model, _BaseModel):
    """项目信息表"""
    __tablename__ = 'dm_docker_container'
    id = Column(INTEGER, primary_key=True)
    docker_id = Column(String(32))
    project_id = Column(String(32))
    container_id = Column(String(32))
    git_address = Column(String(64))
    git_branch = Column(String(32))
    image_name = Column(String(32))
    net_name = Column(String(32))
    net_ip = Column(String(32))
    creator_id = Column(String(32))


def insert_docker_container(docker_dict):
    """新建docker容器记录"""
    docker_obj = ModelDockerContainer()
    docker_obj.docker_id = gen_unique_id()
    docker_obj.project_id = docker_dict.get('project_id')
    docker_obj.container_id = docker_dict.get('container_id', '')
    docker_obj.git_address = docker_dict.get('git_address')
    docker_obj.git_branch = docker_dict.get('git_branch')
    docker_obj.image_name = docker_dict.get('image_name')
    docker_obj.net_name = docker_dict.get('net_name')
    docker_obj.net_ip = docker_dict.get('net_ip')
    docker_obj.creator_id = docker_dict.get('creator_id')

    db.session.add(docker_obj)
    db.session.commit()
    return 0, 'success'


