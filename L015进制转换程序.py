
while 1:
    temp=input('请输入一个整数/(输入Q结束程序/):')
    if temp == 'Q' or temp == 'q':
        break
    else:
        num = int(temp)
        print('十进制 -> 十六进制：'+temp+' -> '+ str('%x' % num))
        print('十进制 -> 八进制：'+temp+' -> '+ str('%o' % num))
        print('十进制 -> 二进制：'+temp+' -> '+ str(bin(num)))
