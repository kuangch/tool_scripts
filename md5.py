import argparse
import os
import hashlib

def get_file_md5(file_name):
    """
    计算文件的md5
    :param file_name:
    :return:
    """
    m = hashlib.md5()   #创建md5对象
    with open(file_name,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  #更新md5对象

    return m.hexdigest()    #返回md5对象

def gen_all_file_md5(dir_path):
    dir_path = os.path.abspath(dir_path)
    if os.path.isfile(dir_path):
        # 文件
        root = os.path.dirname(dir_path)
        file = os.path.basename(dir_path)
        with open(str(root + os.sep + file + '.md5'), 'w') as md5file:
            md5file.writelines(f'{get_file_md5(dir_path)} \n')
            md5file.close()

    else:
        # 目录
        for root, dirs, files in os.walk(dir_path):
            md5s = []
            for file in files:
                if 'md5s.txt' in file:
                    continue
                md5s.append({'file': file, 'md5': get_file_md5(str(root + '/' + file))})

            with open(str(root + '/md5s.txt'), 'w') as md5file:
                for md5 in md5s:
                    md5file.writelines(f'{md5["file"]} : {md5["md5"]} \n')
                md5file.close()


if __name__ == "__main__":

    import sys
    dir = sys.argv[1]
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-p', '--path', required=False, default='./', help='要计算md5值的路径或者文件')
    # args = parser.parse_args()

    gen_all_file_md5(dir)