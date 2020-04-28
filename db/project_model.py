"""project数据库操作类"""
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.exc import IntegrityError

from db.base_model import db, _BaseModel
from common_tool import gen_unique_id
from flask import current_app


class ModelProject(db.Model, _BaseModel):
    """项目信息表"""
    __tablename__ = 'dm_project'
    id = Column(INTEGER, primary_key=True)
    project_id = Column(String(32))
    project_name = Column(String(32))
    project_description = Column(String(64))
    project_creator_id = Column(String(32))


def insert_project(project_dict):
    """新建项目信息记录"""
    project_obj = ModelProject()
    project_obj.project_id = gen_unique_id()
    project_obj.project_name = project_dict.get('project_name', '')
    project_obj.project_description = project_dict.get('project_description', '')
    project_obj.project_creator_id = project_dict.get('project_creator_id', '')
    try:
        db.session.add(project_obj)
        db.session.commit()
    except IntegrityError as e:
        current_app.logger.info('exception= {}'.format(e))
        return 202004251120, 'duplicate project name'
    return 0, 'success'


