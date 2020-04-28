"""启动配置类"""
from flask import Flask
import logging
from flask_log_request_id import RequestID, RequestIDLogFilter
from logging.handlers import TimedRotatingFileHandler
from api.project_api import project_blue
from api.docker_api import docker_blue
from db.base_model import db

app = Flask(__name__)

RequestID(app)
LOG_PATH = 'log/app.log'
HANDLER = TimedRotatingFileHandler(LOG_PATH, when="D", interval=1, backupCount=30)
FORMATTER = logging.Formatter("[%(asctime)s][%(request_id)s] [%(pathname)s:%(lineno)d] %(levelname)s - %(message)s")
HANDLER.setFormatter(FORMATTER)
HANDLER.addFilter(RequestIDLogFilter())
app.logger.addHandler(HANDLER)
app.logger.setLevel(logging.DEBUG)

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1/dockermanager"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1/dockermanager"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db.init_app(app)


app.register_blueprint(project_blue)
app.register_blueprint(docker_blue)

if __name__ == '__main__':
    app.run()
