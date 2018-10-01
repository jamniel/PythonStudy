file_name = input('请输入文件名：')

file = open(file_name, 'x', encoding='utf8')
print('请输入内容【单独输入\':w\'保存退出】：')

while 1:
    file_content = input()
    if file_content != ':w':
        file.write('%s\n' % file_content)
    else:
        break
file.close()
