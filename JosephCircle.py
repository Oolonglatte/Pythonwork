

def josephCircle(all_number,counters,q=4):
    a=[0]*all_number
    k=count=i=0
    while(count!=counters):   
        if(i>(all_number-1)):
            i=0
        if(a[i]==0):#判断是否还在组内#
            k+=1
            if(k==q):
                a[i]=1  #标记
                count+=1
                print(i)
                k=0
        i+=1
    #result=a.index(0)
    #print(result)
    print(a)
    print(a.index(0))
    return 0

if __name__ == '__main__':
    josephCircle(10,9)
    