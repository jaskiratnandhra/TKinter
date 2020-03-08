from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
a=Tk()
a.title('tk')
reg=Label(a,text="REGNO")
regtxt=Entry(a,width=10)
reg.grid(column=0,row=0)
regtxt.grid(column=1,row=0)

name=Label(a,text="NAme")
nametxt=Entry(a,width=10)
name.grid(column=0,row=1)
nametxt.grid(column=1,row=1)

dept=Label(a,text="Dept")
depttxt=Entry(a,width=10)
dept.grid(column=0,row=2)
depttxt.grid(column=1,row=2)

gen=Label(a,text="Gender")
gen.grid(column=0,row=3)
i=IntVar()
ra1=Radiobutton(a,text="MALE",value=1,variable=i)
ra2=Radiobutton(a,text="FEMALE",value=2,variable=i)
se=i.get()
gen=''
def c():
    se=i.get()

    if(se==1):
        gen='MALE'
    else:
        gen='FEMALE'
    return gen
ra1.grid(column=1,row=3)
ra2.grid(column=2,row=3)

age=Label(a,text="age")
w = Spinbox(a, from_=10, to=100)

age.grid(column=0,row=4)
w.grid(column=1,row=4)

con = connect('myTable.db')
cur = con.cursor()
try:
    cur.execute("""CREATE TABLE student(
    reg INTEGER,
    name VARCHAR(20),
    dept VARCHAR(20),
    gender VARCHAR(20),
    age INTEGER);""")
except OperationalError: 
    None

def insert():
    a=c()
    cur.execute("""INSERT INTO student(reg,name,dept,gender,age) VALUES(?,?,?,?,?);""",(regtxt.get(),nametxt.get(),depttxt.get(),a,w.get()))
    

b1=Button(a,text='Insert',command=insert)
def update():
    a=c()
    cur.execute("""UPDATE student SET name=?,dept=?,gender=?,age=? WHERE reg=?;""",(nametxt.get(),depttxt.get(),a,w.get(),regtxt.get()))
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

b1.grid(column=0,row=5)
b2.grid(column=1,row=5)
b3.grid(column=0,row=6)
b4.grid(column=1,row=6)

con.commit()
#con.close()

a.mainloop()
