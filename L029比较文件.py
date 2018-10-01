def dif_file(file_name1, file_name2):
    
    f1=open(file_name1, 'r', encoding='utf8')
    f2=open(file_name2, 'r', encoding='utf8')
    line = 0
    diff_line = list()

    while 1:
        f1_content = f1.readline()
        f2_content = f2.readline()
        line += 1
        if (f1_content == '' and f2_content == ''):
            break
        elif f1_content == f2_content:
            continue
        else:
            diff_line.append(line)

    f1.close()
    f2.close()

    print('两个文件共有【%d】处不同：' % len(diff_line))

    for each in diff_line:
        print('第%d行不一样' % each)


file_1=input('请输入需要比较的头一个文件名：')
file_2=input('请输入需要比较的另一个文件名：')

dif_file(file_1,file_2)
