contact = dict()

print('''|--- 欢迎进入通讯录程序 ---|
|--- 1:查询联系人资料 ----|
|--- 2:插入新的联系人 ----|
|--- 3:删除已有联系人 ----|
|--- 4:退出通讯录程序 ----|''')

instructor = 0
while instructor != 4:
    instructor = int(input('请输入相关的指令代码：'))
    if instructor == 4:
        break
    elif instructor == 1:
        name1 = input('请输入联系人姓名：')
        if name1 in contact:
            print('%s:%s' % (name1, contact[name1]))
        else:
            print('您输入的姓名在通讯录中不存在')
    elif instructor == 2:
        name2 = input('请输入联系人姓名：')
        if name2 in contact:
            print('您输入的姓名在通讯录中已存在 -->> %s : %s' % (name2, contact[name2]))
            if_modify = input('是否修改用户资料(YES/NO):')
            if if_modify == 'YES' or if_modify == 'yes':
                contact[name2] = input('请输入用户联系电话：')
        else:
            contact[name2] = input('请输入用户联系电话：')
    elif instructor == 3:
        name3 = input('请输入要删除的联系人姓名：')
        if name3 in contact:
            del contact[name3]
            print('%s已被删除！' % name3)
        else:
            print('该用户不存在')
    else:
        print('您输入的指令错误')


print('|---感谢使用通讯录程序---|')
