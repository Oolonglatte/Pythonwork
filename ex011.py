# 敏感词文本文件 filtered_words.txt，里面的内容为每一行一个敏感词。 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
# 分为两个函数部分 获得敏感词  获得用户输入并判别

def filtered_words(words_file):
    with open(words_file,"r",encoding="utf-8") as f:
        words = f.readlines()
        filtered_words=[]
    for line in words:
        line=line.rstrip('\n')  # Python strip() 方法用于移除字符串头尾指定的字符(默认为空格或换行符)
        filtered_words.append(line)
    f.close()
    #print(filtered_words)
    return filtered_words

def WordsFiler(list):
    str_for_check=input('请输入要查找的字符串：')
    if str_for_check in list:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    WordsFiler(filtered_words('filtered_words.txt'))
