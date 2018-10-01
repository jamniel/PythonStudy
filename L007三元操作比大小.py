print('------------使用三元操作取最小---------------')
x, y, z = 6, 5, 4
if x<y<z or x<z<y:
    small=x
elif y<z<x or y<x<z:
    small=y
else:
    small=z
