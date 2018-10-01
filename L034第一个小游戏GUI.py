import random
import easygui as g

secret = random.randint(1, 10)
g.msgbox('------------------我爱鱼C工作室------------------')

try:
    temp = g.enterbox('不妨猜一下小甲鱼现在心里想的是哪个数字：', '猜数字小游戏')

except (EOFError, KeyboardInterrupt):
    g.msgbox('输入错误')

else:
    while 1:
        try:
            guess = int(temp)
            break
        except ValueError:
            temp = g.enterbox('您输入不是数字，请重新输入', '猜数字小游戏')

    while guess != secret:
        temp = g.enterbox("哎呀，猜错了，请重新输入吧：", "猜数字小游戏")
        while 1:
            try:
                guess = int(temp)
                break
            except ValueError:
                temp = g.enterbox('您输入不是数字，请重新输入', '猜数字小游戏')
        if guess == secret:
            g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
            g.msgbox("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                g.msgbox("哥，大了大了~~~")
            else:
                g.msgbox("嘿，小了，小了~~~")
    g.msgbox("游戏结束，不玩啦^_^")

