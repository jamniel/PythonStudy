import os
import os.path

def search_file(start_dir, target_file):
    os.chdir(start_dir)
    file_list = os.listdir(os.curdir)
    for each_file in file_list:
        if os.path.isfile(each_file) and each_file == target_file:
            print(os.getcwd()+os.sep+each_file)
        if os.path.isdir(each_file):
            search_file(each_file, target_file)
            os.chdir(os.pardir)

start_dir = input('请输入待查找的初始目录：')
target_file = input('请输入需要查找的目标文件：')
search_file(start_dir, target_file)

