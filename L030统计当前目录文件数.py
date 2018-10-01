import os
import os.path

def count_file(dir_path):

    file_dir_list = os.listdir(path=dir_path)
    file_count_dict = dict()

    for file_name in file_dir_list:
        if os.path.isdir(dir_path + '/' + file_name):
            file_count_dict.setdefault('文件夹', 0)
            file_count_dict['文件夹'] += 1
        else:
            ext = os.path.splitext(file_name)[1]
            file_count_dict.setdefault(ext, 0)
            file_count_dict[ext] += 1

    for each_key in file_count_dict.keys():
        print('该文件夹下共有类型为【%s】的文件%d个' % (each_key, file_count_dict[each_key]))

cur_path = input('本脚本用于计算文件夹内各文件类型数量，请输入文件夹绝对路径：')

count_file(cur_path)




