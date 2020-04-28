from common_tool import gen_unique_id
import os

ROOT_DIR = 'static/shell/'


def test():
    """测试调用脚本 echo输出"""
    sh_file_path = ROOT_DIR + 'test.sh'
    os.system('sh ' + sh_file_path + ' aaa')


def test_git_pull():
    """调用脚本 从git拉取java项目，并创建镜像启动"""
    sh_file_path = ROOT_DIR + 'centos_jdk_test.sh'
    git_address = 'https://github.com/gfffbjtu/SpringBootTest.git'
    git_branch = 'master'
    image_name = 'dockerjava:v3'
    param_arr = ['sh', sh_file_path, git_address, git_branch, image_name]
    os.system(' '.join(param_arr))


def build_java_project_image(image_dict):
    sh_file_path = ROOT_DIR + 'build_java_image.sh'
    git_address = image_dict['git_address']
    git_branch = image_dict['git_branch']
    image_name = image_dict['image_name']
    tmp_file = gen_unique_id()
    param_arr = ['sh', sh_file_path, git_address, git_branch, image_name, '>', tmp_file]
    os.system(' '.join(param_arr))
    param_arr = ['cat', tmp_file, '|', 'awk', '\'END {print}\'']
    tail_line = os.system(' '.join(param_arr))
    return ' '.split(tail_line)[-1]


if __name__ == '__main__':
    test_git_pull()


