import hashlib
import uuid
import json
from flask import request, current_app


def gen_unique_id():
    """获取唯一id"""
    return do_gen_unique_id(str(uuid.uuid4()))


def do_gen_unique_id(data_str):
    """ 根据字符串内容生成唯一标志 md5 """
    md5_str = calculate_md5(data_str.encode())
    _data_str = "91a667200d33c146ffd484ac357f0b26" + md5_str
    return calculate_md5(_data_str.encode())


def calculate_md5(byte_buf):
    """ 给字节数据计算 md5 返回str """
    m = hashlib.md5()
    m.update(byte_buf)
    return m.hexdigest()


def get_request_json_obj():
    """获取json请求参数,并将其转换为对象"""
    if request.method != 'GET':
        req_json = request.json
        request_body = json.dumps(req_json, ensure_ascii=False)
        current_app.logger.info("request_body=%s", request_body)
        return json.loads(request_body)


if __name__ == '__main__':
    print(gen_unique_id())
