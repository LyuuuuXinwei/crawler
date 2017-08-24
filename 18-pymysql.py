import pymysql

'''mysql.connector--MySQL官方连接库，作用类似'''
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='2981826123',db='scraping',charset='utf8') #localhost和127.0.0.1都行
cur=conn.cursor() #建立连接后如果要操作多个数据库可以创建多个光标
cur.execute('USE scraping')

cur.execute('SELECT * FROM pages WHERE id=1')
print(cur.fetchone()) #fetchone返回最后一次查询结果
cur.close()
conn.close()