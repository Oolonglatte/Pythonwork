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

def WordsInput(list):
    str_for_check=input('请输入字符串：')
    for each in list:
        i=len(each)
        rep_word='*'*i
        str_for_check=str_for_check.replace(each,rep_word)
    print(str_for_check)
    return 0


if __name__ == '__main__':
    WordsInput(filtered_words('filtered_words.txt'))
