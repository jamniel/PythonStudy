file_name = input('请输入要打开的文件（C:\\\\test.txt）：')
line_range = input('请输入需要显示的行数【格式如13:21或:21或21:】：')
line_range_dict = line_range.split(':')

# 确认行号并显示
file_content = open(file_name, 'r')
if line_range_dict[0] != '' and line_range_dict[1] != '':
    line_start = int(line_range_dict[0])-1
    line_end = int(line_range_dict[1])
    print('\n文件%s的从第%d行到第%d行的内容如下：\n' % (file_name, line_start, line_end))
    for line in file_content.readlines()[line_start:line_end]:
        print(line)


elif line_range_dict[0] == '' and line_range_dict[1] != '':
    line_end = int(line_range_dict[1])
    print('\n文件%s的从开始到第%d行的内容如下：\n' % (file_name, line_end))
    for line in file_content.readlines()[:line_end]:
        print(line)

elif line_range_dict[0] != '' and line_range_dict[1] == '':
    line_start = int(line_range_dict[0])-1
    print('\n文件%s的从第%d行到最后的内容如下：\n' % (file_name, line_start))
    for line in file_content.readlines()[line_start:]:
        print(line)

else:
    print('\n文件%s的全文内容如下：\n' % file_name)
    for each_line in file_content:
        print(each_line)

file_content.close()
