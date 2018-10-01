def get_digits(n):
    result=[]
    if n:
        result = list(get_digits(n // 10))
        return result+ list(n%10)
    else:
        return result

print(get_digits(12345))
