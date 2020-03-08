from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
a=Tk()
a.title('tk')
reg=Label(a,text="Bookingid")
regtxt=Entry(a,width=10)
reg.grid(column=0,row=0)
regtxt.grid(column=1,row=0)

name=Label(a,text="Passenger Name")
nametxt=Entry(a,width=10)
name.grid(column=0,row=1)
nametxt.grid(column=1,row=1)

dept=Label(a,text="Flight")
depttxt=Entry(a,width=10)
dept.grid(column=0,row=2)
depttxt.grid(column=1,row=2)

gen=Label(a,text="Source")
gen.grid(column=0,row=3)
i=IntVar()
ra1=Radiobutton(a,text="Delhi",value=1,variable=i)
ra2=Radiobutton(a,text="Mumbai",value=2,variable=i)
se=i.get()
gen=''
def c():
    se=i.get()

    if(se==1):
        gen='Delhi'
    else:
        gen='Mumbai'
    return gen
ra1.grid(column=1,row=3)
ra2.grid(column=2,row=3)

e=Label(a,text="Destination")
e.grid(column=0,row=4)
b=IntVar()
ra3=Radiobutton(a,text="Chennai",value=1,variable=b)
ra4=Radiobutton(a,text="Kolkata",value=2,variable=b)
se=b.get()
des=''
def o():
    se=b.get()

    if(se==1):
        des='Chennai'
    else:
        des='Kolkata'
    return des
ra3.grid(column=1,row=4)
ra4.grid(column=2,row=4)




age=Label(a,text="Duration")
w = Spinbox(a, from_=10, to=100)

age.grid(column=0,row=5)
w.grid(column=1,row=5)

con = connect('myTable.db')
cur = con.cursor()
try:
    cur.execute("""CREATE TABLE student(
    reg INTEGER,
    name VARCHAR(20),
    dept VARCHAR(20),
    gender VARCHAR(20),
    des VARCHAR(20),
    age INTEGER);""")
except OperationalError: 
    None

def insert():
    a=c()
    p=o()
    cur.execute("""INSERT INTO student(reg,name,dept,gender,des,age) VALUES(?,?,?,?,?,?);""",(regtxt.get(),nametxt.get(),depttxt.get(),a,p,w.get()))
    

b1=Button(a,text='Insert',command=insert)
def update():
    a=c()
    p=o()
    cur.execute("""UPDATE student SET name=?,dept=?,gender=?,des=?,age=? WHERE reg=?;""",(nametxt.get(),depttxt.get(),a,p,w.get(),regtxt.get()))
b2=Button(a,text='Update',command=update)
def delete():
    cur.execute("""DELETE FROM student WHERE reg=?;""",(regtxt.get(),))
    
b3=Button(a,text='Delete',command=delete)
def select():
    cur.execute("""SELECT * FROM student WHERE reg=?;""",(regtxt.get(),))
    ans=cur.fetchall()
    for i in ans:
        print(ans)
    
b4=Button(a,text='Select',command=select)

b1.grid(column=0,row=6)
b2.grid(column=1,row=6)
b3.grid(column=0,row=7)
b4.grid(column=1,row=7)

con.commit()
#con.close()

a.mainloop()
