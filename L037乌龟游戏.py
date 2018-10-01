import random

class Turtle:
    def __init__(self):
        self.hp = 100
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):

        if random.choice('xy') == 'x':               # 选择随机方向
            self.x += random.choice([-2, -1, 1, 2])  # 随机移动步数
            if self.x < 0:
                self.x = -self.x
            if self.x > 10:
                self.x = 10 - (self.x - 10)
        else:
            self.y += random.choice([-2, -1, 1, 2])
            if self.y < 0:
                self.y = -self.y
            if self.y > 10:
                self.y = 10 - (self.y - 10)
        self.hp -= 1

        return self.x, self.y

class Fish:

    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        if random.choice('xy') == 'x':  # 选择随机方向
            self.x += random.choice([-1, 1])  # 随机移动步数
            if self.x < 0:
                self.x = -self.x
            if self.x > 10:
                self.x = 10 - (self.x - 10)
        else:
            self.y += random.choice([-1, 1])
            if self.y < 0:
                self.y = -self.y
            if self.y > 10:
                self.y = 10 - (self.y - 10)
        return self.x, self.y

begin = input('这是一个乌龟吃鱼的游戏，输入【Y】开始游戏：')

if begin == 'Y':
    turtle = Turtle()

    # 生成10条鱼，并将位置元祖存入列表fish中。
    fish = []
    for i in range(10):
        newfish = Fish()
        fish.append(newfish)

    print('乌龟的初始位置是(%d,%d)' % (turtle.x, turtle.y))

    # 输出所有小鱼的位置
    print('小鱼的初始位置是')
    for each_fish in fish:
        print('(%s,%s)' % (each_fish.x, each_fish.y), end='')

    print('\n乌龟的初始体力为：%d' % turtle.hp)
    trigger = input('回车开始移动,输入其他退出：')

    while trigger == '':
        pos = turtle.move()
        if turtle.hp < 0:
            print('乌龟没有体力了！！！')
            break
        if len(fish):
            print('鱼吃光了！！！')
            break

        # 吃鱼
        for each_fish in fish:
            if each_fish.move() == pos:
                turtle.hp = 100 if (turtle.hp + 20) > 100 else (turtle.hp + 20)
                fish.remove(each_fish)
                print('鱼被吃了')

        print('乌龟的位置是【%d，%d】' % (turtle.x, turtle.y))

        # 输出所有小鱼的位置
        print('小鱼的位置是')
        for each_fish in fish:
            print('(%s,%s)' % (each_fish.x, each_fish.y), end='')

        print('\n乌龟的体力为：%d' % turtle.hp)
        trigger = input('回车继续移动,输入其他退出：')

print('Game Over')
