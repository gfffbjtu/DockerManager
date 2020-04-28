from flask import Blueprint, jsonify, current_app
from common_tool import get_request_json_obj
from db.project_model import insert_project

project_blue: Blueprint = Blueprint('project_api', __name__)


@project_blue.route('/')
def hello_world():
    current_app.logger.info('hello')
    return 'Hello World!'


@project_blue.route('/project/add', methods=['POST'])
def create_project():
    """新建项目"""
    create_project_req_json = get_request_json_obj()

    project_dict = {"project_name": create_project_req_json['project_name']}
    err_no, err_msg = insert_project(project_dict)

    return jsonify({'err_no': err_no, 'err_msg': err_msg})



