from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect as _inspect


# 创建数据库的操作对象
# 在这里初始化SQLAlchemy对象，可以避免project_api与main的循环引用
db = SQLAlchemy()
# db: SQLAlchemy = SQLAlchemy(app, session_options={'autocommit': True})


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
