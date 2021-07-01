import random,string
CharsforSelect=string.ascii_letters + string.digits
#ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9.
def generate(count,length):
    list1=[]
    for x in range(count):
        re=''
        for y in range(length):
            re+=random.choice(CharsforSelect)
        print(re)
        list1.append(re)
    return list1
#通过列表的方式返回可以方便后面的使用#

if __name__ == '__main__':
    list2=generate(4,3)
    print(CharsforSelect)
    print(list2)
