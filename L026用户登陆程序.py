login = dict()

while 1:
    instr = input('''|--- 新建用户：N/n ---|
|--- 登陆账号：E/e ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码：''')

    if instr == 'N' or instr == 'n':
        name = input('请输入用户名：')
        while name in login:
            name = input('此用户名已经被使用，请重新输入：')
        else:
            pwd = input('请输入密码：')
            login[name] = pwd
            print('注册成功，赶紧试试登陆吧^_^\n')

    if instr == 'E' or instr == 'e':
        name = input('请输入用户名：')
        while name not in login:
            name = input('您输入的用户名不存在，请重新输入：')
        else:
            pwd = input('请输入密码：')
            if login.get(name) == pwd:
                print('欢迎使用xxoo系统，请点右上角的x结束程序！')
                break
            else:
                print('您输入的密码错误！')
                break

    if instr == 'Q' or instr == 'q':
        break

    else:
        continue
   
    
