import os

ROOT_DIR = 'static/shell/'


def test():
    sh_file_path = ROOT_DIR + 'test.sh'
    os.system('sh ' + sh_file_path + ' aaa')


if __name__ == '__main__':
    test()