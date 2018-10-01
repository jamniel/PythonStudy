#分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。
def count(*str1):
    str_num = 1
    for each_str in str1:
        alpha_num = 0
        space_num = 0
        digit_num = 0
        other_num = 0
        for each_char in each_str:
            if each_char.isalpha():
                alpha_num += 1
            elif each_char.isdigit():
                digit_num += 1
            elif each_char.isspace():
                space_num += 1
            else:
                other_num += 1
        print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个' % (str_num, alpha_num, digit_num, space_num, other_num))
        str_num +=1

    
count('I love you','welcome to china@google.com', '13 plus 26 is 39.') 
