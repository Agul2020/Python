from tkinter import *
from tkinter.ttk import *
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()
port = 8088
s.connect((host, port))
msg = s.recv(1024)



print (msg.decode())


window = Tk()
window.title("First Window")
window.geometry("400x400")

lbl_name = Label(window, text="员工信息录入",font=("Arial Bold", 30))
lbl_name.grid(column=2, row=1)


lbl_name = Label(window, text="姓名")
lbl_name.grid(column=0, row=2)
txt_name = Entry(window, width=10)
txt_name.grid(column=1, row=2)

lbl_age = Label(window, text="年龄")
lbl_age.grid(column=0, row=3)
spin_age = Spinbox(window, from_=0, to=130, width=10)
spin_age.grid(column=1, row=3)

lbl_address = Label(window, text="地址")
lbl_address.grid(column=0, row=4)
txt_address = Entry(window, width=10)
txt_address.grid(column=1, row=4)

lbl_salary = Label(window, text="薪资")
lbl_salary.grid(column=0, row=5)
spin_salary = Spinbox(window, from_=0, to=10000000, width=10)
spin_salary.grid(column=1, row=5)

def clicked():
    res =txt_name.get() +' '+ spin_age.get() +' ' + txt_address.get()+' ' +spin_salary.get()
    # print(str(res))
    s.send(res.encode())
    s.close()


btn1 = Button(window, text="录入信息", command=clicked)
btn1.grid(column=1, row=6)

lbl_name = Label(window, text=msg.decode())
lbl_name.grid(column=1, row=7)

window.mainloop()