#本脚本用来判断给定年份是否为闰年
print('------本脚本用来判断给定年份是否为闰年--------')
print('请输入需要判断的年份：', end=' ')
temp = input()
while not (temp.lstrip('-')).isdigit():
    print('Please input a valid year:', end=' ')
    temp = input()
year = int(temp)
if -9999 <= year <= 9999:
    if (year%400==0):
        print(temp + '是闰年')
    else:
        if (year%4==0 and year%100 !=0):
            print(temp + '是闰年')
        else:
            print(temp + '不是闰年')
else:
    print('您输入的年份太遥远拉...')

