member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
n=0
for i in member:
    if n%2 ==0:
        print(i, end=' ')
        n+=1
    else:
        print(i)
        n+=1
