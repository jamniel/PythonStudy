print('--------------本脚本用来计算分数对应的成绩----------------')
temp = input('请输入您的成绩<0-100>:')
while (not temp.isdigit()):
    print('请输入0-100的分数:', end=' ')
    temp = input()
point = int(temp)
if (60 <= point < 80):
    print('您的成绩是:C')
elif (80 <= point < 90):
    print('您的成绩是:B')
elif (point < 60):
    print('您的成绩是:D')
elif (90 <= point <= 100):
    print('您的成绩是:A')
else:
    print('您输入的数字不在0-100内。')
