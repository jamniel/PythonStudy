import os
import os.path

def pos_in_line(line, key):
    begin = line.find(key)
    pos = []
    while begin != -1:
        pos.append(begin)
        begin = line.find(key, begin+1)
    return pos

def search_in_file(file_name, key):
    f = open(file_name)
    count = 0
    key_dict = dict()
    for each_line in f:
        count += 1
        pos = pos_in_line(each_line, key)
        if pos:
            key_dict[count] = pos
    f.close()

    return key_dict

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for each_key in keys:
        print('关键字出现在%s行，第%s个位置' % (each_key, str(key_dict[each_key])))


def search_keywords(keys):
    all_file = os.walk(os.getcwd())
    file_path = []
    for each_dir in all_file:
        for each_file in each_dir[2]:
            if os.path.splitext(each_file)[1] == '.txt':
                each_file = os.path.join(each_dir[0], each_file)
                file_path.append(each_file)

    for each_txt_file in file_path:
        key_dict = search_in_file(each_txt_file, keys)
        if key_dict:
            print('在文件【%s】中查询到关键字【%s】。' %(each_txt_file, keys) )
            print_pos(key_dict)

key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')

search_keywords(key)

