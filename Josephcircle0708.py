class people():
    flag=0 #是否被排出的标志位
    def __init__(self,name,id,gender):
        self.name = name
        self.id = id
        self.gender = gender

sky=people('sky','2020****','男')
csb=people('csb','2020****','男')
yyj=people('yyj','2020****','男')
wyk=people('wyk','2020****','男')
hht=people('hht','2020****','男')
wf=people('wf','2020****','男')
cn=people('cn','2020****','男')
hh=people('hh','2020****','男')

group_list=[sky,csb,yyj,wyk,hht,wf,cn,hh]

def add_people_to_list(person,list):
    list=[]
    list.append(person)
    return list

def JosephCircle(group_list,counters,interval=4): # q 改为 interval 注意命名规范
    k=count=i=0  # k：计数循环，count：计排除人数，i：list中的索引位置

    while(count!=counters):   
        if(i>(len(group_list)-1)):
            i=0
        if(group_list[i].flag==0):#判断是否还在组内#  
            k+=1
            if(k==interval):
                group_list[i].flag=1  #标记
                count+=1
                print(group_list[i].name +'被排出')
                k=0
        i+=1

    #print(group_list[i].name)


    #遍历一下找一找幸存着
    for a in range(0,len(group_list)):
        if (group_list[a].flag==0):
            surviver=group_list[a]
            print(surviver.name+'幸存')
    
   
    return 0


if __name__ == '__main__':
    JosephCircle(group_list,7,3)


    
