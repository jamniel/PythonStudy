def gcd(x,y):
    if y > x:
        t=x
        x=y
        y=t
    r1=x%y
    while r1:
        x=y
        y=r1
        r1=x%y
    return y
