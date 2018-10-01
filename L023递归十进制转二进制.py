def dec2bin(x):
    result = ''    
    if x:
        result = dec2bin(x//2)
        return result + str(x % 2)   
    else:
        return result
