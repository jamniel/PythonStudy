# calculate the times of a 2bit sub sting in a long sting.
def findstr(short_str, long_str):
    return long_str.count(short_str)

str1=input('请输入目标字符串：')
substr1=input('请输入子字符串（两个字符）：')
times = findstr(substr1, str1)
print('子字符串在目标字符串中共出现%d次' % times)
