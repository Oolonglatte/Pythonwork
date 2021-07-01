import pymysql
from ex001 import generate

def StoreListIntoMysql(list):
    #链接数据库#
    conn = pymysql.connect(
        host ='rm-wz9d4iopy2m6549id8o.mysql.rds.aliyuncs.com',
        port =3306,
        user ='qimu_0527',
        passwd = 'qimu_0527',
        db = 'shoukaiyuan'
    )
    cur=conn.cursor()
    #创建Table 并导入数据#
    cur.execute('''create table Listofgenerate(
         id int not null auto_increment, 
         code VARCHAR(25) not null,
         primary key(id)

        )''')
    for code in list:
        cur.execute('insert into Listofgenerate(code) values(%s)',(code))
        cur.connection.commit()
   #关闭连接# 
    cur.close()
    conn.close()



if __name__ == '__main__':
    a=generate(200,20)
    StoreListIntoMysql(a)
