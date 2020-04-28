from flask import Blueprint, jsonify, current_app
from common_tool import get_request_json_obj
from db.docker_model import insert_docker_container

docker_blue: Blueprint = Blueprint('docker_api', __name__)


@docker_blue.route('/docker/add', methods=['POST'])
def create_docker():
    """新建容器"""
    create_docker_req = get_request_json_obj()
    # 非空参数校验
    if 'project_id' in create_docker_req:
        project_id = create_docker_req['project_id']
    else:
        return jsonify({'err_no': 202004280848, 'err_msg': 'param error-project_id cannot be null'})
    if 'image_name' in create_docker_req:
        image_name = create_docker_req['image_name']
    else:
        return jsonify({'err_no':202004280848, 'err_msg': 'param error-image_name cannot be null'})

    docker_dict = {
        'project_id': project_id,
        'image_name': image_name,
        'git_address': create_docker_req.get('git_address', ''),
        'git_branch': create_docker_req.get('git_branch', 'master'),
        'net_name': create_docker_req.get('net_name', ''),
        'net_ip': create_docker_req.get('net_ip', ''),
        'creator_id': create_docker_req.get('creator_id', '')
    }

    err_no, err_msg = insert_docker_container(docker_dict)
    return jsonify({'err_no': err_no})
