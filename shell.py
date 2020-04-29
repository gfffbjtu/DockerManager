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
    """调用脚本 从git拉取java项目,返回生成的镜像id"""
    sh_file_path = ROOT_DIR + 'build_java_image.sh'
    git_address = image_dict['git_address']
    git_branch = image_dict['git_branch']
    image_name = image_dict['image_name']
    tmp_file = gen_unique_id()
    param_arr = ['sh', sh_file_path, git_address, git_branch, image_name, '>', tmp_file]
    os.system(' '.join(param_arr))
    file = open(tmp_file)
    lines = file.readlines()
    tail_line = lines[-1]
    os.system('rm -rf ' + tmp_file)
    image_id = tail_line.split(' ')[-1]
    if image_id.endswith('\n'):
        return image_id[0: -2]
    return image_id


if __name__ == '__main__':
    image_id = '9ff41025cdf3\n'
    if image_id.endswith('\n'):
        image_id = image_id[0: -2]
    print(image_id)


