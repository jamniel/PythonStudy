import os
import os.path

def search_file(start_dir, target_ext, store_file):
    os.chdir(start_dir)
    file_list = os.listdir(os.curdir)
    f = open(store_file, 'a')
    for each_file in file_list:
        if os.path.isfile(each_file):
            if os.path.splitext(each_file)[1] in target_ext:

                # 存入文件中
                f.writelines(os.getcwd()+os.sep+each_file + '\n')

        if os.path.isdir(each_file):
            search_file(each_file, target_ext, store_file)
            os.chdir(os.pardir)
    f.close()

start_dir = input('请输入待查找的初始目录：')
target_ext = ['.mp4', '.txt', '.avi']
file_name = input('请输入存储查找结果的文件:')

search_file(start_dir, target_ext, file_name)

