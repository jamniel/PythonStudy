pwd = input('请输入需要检查的密码组合：')

if (pwd.isalnum() or len(pwd) <=8):
    print('''您的密码安全级别评定为：低
             请按以下方式提升您的密码安全级别：
                 1.密码必须由数字、字母及特殊字符三种组合
                 2.密码只能由字母开头
                 3.密码长度不能低于16位''')
