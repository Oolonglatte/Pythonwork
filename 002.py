import random,string
CharsforSelect=string.ascii_letters + string.digits
#ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9.
def generate(count,length):
    for x in range(count):
        re=''
        for y in range(length):
            re+=random.choice(CharsforSelect)
        print(re)

if __name__ == '__main__':
        generate(4,3)
