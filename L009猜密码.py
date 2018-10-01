print('--------------密码尝试错误程序---------------')
n = 3
pwd = '123456'
while n:
    temp = input('请输入密码:')
    if pwd == temp:
        print('密码正确，进入程序......')
        break
    elif ('*' in temp):
        print('密码中不能含有"*"号！您还有',n,'次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有',n-1,'次机会！', end=' ')
        n =n-1
        
