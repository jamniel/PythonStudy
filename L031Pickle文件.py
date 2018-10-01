import pickle

def sep_spk(file_name, num):

    f = open(file_name)
    f_boy = open('boy_%d.txt' % num, 'ab')
    f_girl = open('girl_%d.txt' % num, 'ab')
    for each_line in f:
        if each_line[0:3] == '小客服':
            pickle.dump(each_line[4:], f_girl, 0)
        if each_line[0:3] == '小甲鱼':
            pickle.dump(each_line[4:], f_boy, 0)
    f_boy.close()
    f_girl.close()
    f.close()

