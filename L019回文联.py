#判断是否为回文联
def circle_word(fore_word):
    back_word = ''
    list_word = list(fore_word)
    while list_word:
        single_word = list_word.pop()
        back_word += single_word
    if back_word == fore_word:
        return 1
    else:
        return -1

str1=input('请输入一句话：')
print('是回文联！') if circle_word(str1)==1 else print('不是回文联！')
