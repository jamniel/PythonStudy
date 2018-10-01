print('————————爱因斯坦的阶梯——————————')
n=0
while not((n%2 == 1) and (n%3 == 2) and (n%5 == 4) and (n%6 == 5) and (n%7 == 0)):
    n += 1
print ('答案是',n)
