# import sqlite3
# conn = sqlite3.connect('test.db')
# c = conn.cursor()  
# print ("数据库打开成功")   
# c.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)  VALUES (5,'王五',18,'中国',1234)")
# conn.commit()
# print ("数据插入成功")
# conn.close()

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("数据库打开成功")

cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("数据操作成功")
conn.close()


# str = '你好 18 我 她 145'

# x = str.split()

# print(x) 