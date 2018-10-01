#计算各位数的立方和
def cubic_sum(number1):
    length= len(str(number1))
    total = 0
    while length:
        total += (number1 // 10**(length-1))**3
        number1 = number1 % 10**(length-1)
        length -= 1
    return total

number = 100
result = []
while number < 1000:
    if number == cubic_sum(number):
        result.append(number)
    number += 1

print('3位数的水仙花数有：',result)
