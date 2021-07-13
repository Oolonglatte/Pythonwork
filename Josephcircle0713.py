import csv
import xlrd


#建立个体所对应的类
class Person():
    joseph_flag=0 #是否被排出的标志位 默认属性
    def __init__(self,name,school_id,gender):
        self.name = name
        self.school_id = school_id
        self.gender = gender
    def show_student_data(self):
        print("姓名：%s,学号：%s，性别：%s" %(self.name,self.school_id,self.gender))

#父类，默认以txt文本读取
class File_Read(object):
    def __init__(self,path):
        self.path = path

    def get_student_list(self):
        student_list = []
        file = open(self.path,'r',encoding='UTF-8')
        file_by_lines = file.readlines()
        for line in file_by_lines:
            line = line.split()
            new_student = Person(line[0],line[1],line[2])
            student_list.append(new_student)
        return student_list

#子类，以csv方式读取，覆盖方法get_student_list
class File_Read_Csv(File_Read):
    def get_student_list(self):
        student_list = []
        file = open(self.path,'r',encoding='UTF-8')
        file_by_lines = csv.reader(file)
        for line in file_by_lines:
            new_student = Person(line[0],line[1],line[2])
            student_list.append(new_student)
        return student_list

#子类，以excel方式读取,行列遍历获取信息至list
class File_Read_Exc(File_Read):
    def get_student_list(self):
        student_list = []
        file = xlrd.open_workbook(self.path)
        table = file.sheet_by_name('Sheet1') 
        nrows = table.nrows
        for line in range(nrows):
            line_date = table.row_values(line)
            new_student = Person(line_date[0],line_date[1],line_date[2])
            student_list.append(new_student)
        return student_list

#以个体构成列表，约瑟夫环遍历列表
def JosephCircle(person_list,counters,interval=4): # q 改为 interval 注意命名规范
    k=count=i=0  # k：计数循环，count：计排除人数，i：list中的索引位置

    while(count!=counters):   
        if(i>(len(person_list)-1)):
            i=0
        if(person_list[i].joseph_flag==0): #判断是否还在组内#  
            k+=1
            if(k==interval):
                person_list[i].joseph_flag=1  #标记被排出者
                count+=1
                print(person_list[i].name +'被排出') #按顺序打印被排除循环者   
                #person_list[i].show_student_data 写法有问题
                k=0
        i+=1

    #遍历一下list找一找幸存
    for a in range(0,len(person_list)):
        if (person_list[a].joseph_flag==0):
            surviver=person_list[a]
            print(surviver.name+'幸存')
    
    return person_list[:]

if __name__ == '__main__':
    path = r'..\Pythonwork\persondata.xls'
    file = File_Read_Exc(path)
    student_list = file.get_student_list()
    JosephCircle(student_list,7,3)
    
#未完成压缩格式的类型，在面对不同压缩内容时候不知道如何简单的写成一个子类    
