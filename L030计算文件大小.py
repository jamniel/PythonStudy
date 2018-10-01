import os
import os.path

file_list = os.listdir('.')
for each_file in file_list:
    if os.path.isfile(each_file):
        print('%s 【%dBytes】' % (each_file, os.path.getsize(each_file)))
    else:
        continue


