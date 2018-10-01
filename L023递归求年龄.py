def year(n):
    
    if n>1:
        return year(n-1)+2
    
    else:
        return 10

print(year(3))
