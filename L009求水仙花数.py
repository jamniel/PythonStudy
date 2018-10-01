print('------求100~999之间的所有水仙花数------')
n = 100
while n < 1000:
    a=n//100
    b=n//10%10
    c=n%10
    t=a**3+b**3+c**3
    if (t != n):
        n +=1
    else:
        print(n, end='\t')
        n +=1
    
