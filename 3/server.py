from os import name
import socket
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 8088

serversocket.bind((host, port))                                  
print("Server start at port: 8088")

serversocket.listen(5)      



while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("链接地址： %s" % str(addr))

    msg='服务器连接成功！'+ "\r\n"
    clientsocket.send(msg.encode())
    data = clientsocket.recv(1024)
    data=data.decode()
    tuple = data.split()
    print(tuple)
    uid = 6
    uname = tuple[0]
    uage = int(tuple[1])
    uaddress = tuple[2]
    usalary = int(tuple[3])

    c.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES({id},'{name}',{age},'{address}',{salary})".format(id=uid,name=uname,age=uage,address=uaddress,salary=usalary))

    clientsocket.close()
