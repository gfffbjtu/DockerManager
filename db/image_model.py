"""docker数据库操作类"""
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from db.base_model import db, _BaseModel


class ModelImage(db.Model, _BaseModel):
    """镜像信息表"""
    __tablename__ = 'dm_image'
    id = Column(INTEGER, primary_key=True)
    image_id = Column(String(32))
    image_name = Column(String(32))
    git_address = Column(String(64))
    git_branch = Column(String(32))
    creator_id = Column(String(32))


def insert_image(image_dict):
    """新建镜像记录"""
    image_obj = ModelImage()
    image_obj.image_id = image_dict.get('image_id')
    image_obj.image_name = image_dict.get('image_name')
    image_obj.git_address = image_dict.get('git_address')
    image_obj.git_branch = image_dict.get('git_branch')
    image_obj.creator_id = image_dict.get('creator_id')

    db.session.add(image_obj)
    db.session.commit()
    return 0, 'success'


