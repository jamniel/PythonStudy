# this script is to replace certain string in a whole text file

file_name = input('请输入文件名：')
old_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')

file_open = (open(file_name, 'r'))
file_content = file_open.read()
file_open.close()

count = file_content.count(old_word)


print('\n文件%s中共有%d个【%s】' % (file_name, count, old_word))
print('您确认要把所有的【%s】替换为【%s】吗？' % (old_word, new_word))
rep_action = input('【YES/NO】：')

while rep_action not in ('YES', 'Yes', 'yes', 'NO', 'No', 'no'):
    rep_action = input('请输入【YES/NO】：')

if rep_action in ('YES', 'Yes', 'yes'):
    file_open = (open(file_name, 'w'))
    file_open.write(file_content.replace(old_word, new_word))
    file_open.close()
    print('共有%d个%s被替换' % (count, new_word))
else:
    print('未进行替换！')

