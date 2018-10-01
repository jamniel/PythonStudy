def int_input(x):
    while True:
        try:
            temp = int(input(x))
            break
        except ValueError:
            print('出错，您输入的不是整数！')
    return temp

temp = int_input('请输入一个整数：')
print(temp)
