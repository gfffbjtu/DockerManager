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
    image_name = 'dockerjava:v3'
    os.system('sh ' + sh_file_path + ' ' + git_address + ' ' + image_name)


if __name__ == '__main__':
    test_git_pull()
