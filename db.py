"""数据库操作类"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, or_
from sqlalchemy.dialects.mysql import BIGINT, DECIMAL, INTEGER, TIMESTAMP
from sqlalchemy.inspection import inspect as _inspect

from app import app

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1/dockermanager"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1/dockermanager"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
# 创建数据库的操作对象
db: SQLAlchemy = SQLAlchemy(app, session_options={'autocommit': True})


class _BaseModel(object):
    """ _BaseModel """

    def __str__(self):
        return self.to_str()

    def __repr__(self):
        return self.to_str()

    def to_str(self):
        """ to_str """
        column_names = _inspect(self.__class__).columns
        values = ""
        for column in column_names:
            values += str(getattr(self, column.name)) + " "
        return "{}: {}".format(self.__class__.__name__, values)


class ModelProject(db.Model, _BaseModel):
    """项目信息表"""
    __tablename__ = 'dm_project'
    id = Column(INTEGER, primary_key=True)
    project_id = Column(String(32))
    project_name = Column(String(32))
    project_description = Column(String(64))
    project_creator_id = Column(String(32))


def insert_project():
    """新建项目信息记录"""
    db.session.begin(subtransactions=True)
    project_obj = ModelProject()
    project_obj.project_id = '1'
    project_obj.project_name = '测试项目'
    project_obj.project_description = '这是一个测试项目'
    project_obj.project_creator_id = '1'

    db.session.add(project_obj)
    db.session.commit()


if __name__ =='__main__':
    insert_project()
