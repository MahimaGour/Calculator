from tkinter import *

root = Tk()
root.resizable(0,0)
root.configure(bg="lightblue")
root.title("Calculator")

#func
def m1(num):
    temp = input.get()
    templen = len(temp)
    if temp=='0' or temp=="error":
        m2(num)
    else:
        input.insert(templen, num)
    

def m2(val):
    input.delete(0, END)
    input.insert(0, val)

def m3():
    text = input.get()
    try:
        result = eval(text)
        m2(result)
    except:
        m2("error")

def m4():
    x=input.get()
    xlen = len(x)
    input.delete(xlen-1, END)

#input''
input = Entry(root, font=("Arial",15))
input.insert(0, "0")
input.grid(row=1,column=0,columnspan=5, padx=3,ipadx=5, pady=5, ipady=30)


#row1
clear = Button(root, text="C",bg="lightgrey", command=lambda: m2("0"))
clear.grid(row=2,column=0, columnspan=2, padx=3, pady=5, ipadx=42, ipady = 5)
back = Button(root, text="<===",bg="lightgrey", command=m4)
back.grid(row=2,column=2,columnspan=2, padx=3, pady=5, ipadx=27, ipady = 5)
expo = Button(root, text="^",bg="lightgrey", command=lambda: m1("**"))
expo.grid(row=2,column=4, ipadx=13, ipady = 5, padx=3, pady=5)

#row 2
seven = Button(root, text="7",bg="white", command=lambda: m1("7"))
seven.grid(row=3,column=0, padx=3, pady=5, ipadx=12, ipady = 5)
eight = Button(root, text="8",bg="white", command=lambda: m1("8"))
eight.grid(row=3,column=1, ipadx=12, ipady = 5, padx=3, pady=5)
nine = Button(root, text="9", bg="white",command=lambda: m1("9"))
nine.grid(row=3,column=2, ipadx=12, ipady = 5, padx=3, pady=5)

divide = Button(root, text="/",bg="lightgrey", command=lambda: m1("/"))
divide.grid(row=3,column=3, ipadx=15, ipady = 5, padx=3, pady=5)
sqroot = Button(root, text="√",bg="lightgrey", command=lambda: m1("**1/2"))
sqroot.grid(row=3,column=4, ipadx=14, ipady = 5, padx=3, pady=5)

#row3
four = Button(root, text="4", bg="white", command=lambda: m1("4"))
four.grid(row=4,column=0, ipadx=12, ipady = 5, padx=3, pady=5)
five = Button(root, text="5",bg="white", command=lambda: m1("5"))
five.grid(row=4,column=1, ipadx=12, ipady = 5, padx=3, pady=5)
six = Button(root, text="6",bg="white", command=lambda: m1("6"))
six.grid(row=4,column=2, ipadx=12, ipady = 5, padx=3, pady=5)

mul = Button(root, text="X",bg="lightgrey", command=lambda: m1("*"))
mul.grid(row=4,column=3, ipadx=14, ipady = 5, padx=3, pady=5)
inv = Button(root, text="1/x", bg="lightgrey",command=lambda: m1("**(-1)"))
inv.grid(row=4,column=4, ipadx=8, ipady = 5, padx=3, pady=5)

#row4
one = Button(root, text="1",bg="white", command=lambda: m1("1"))
one.grid(row=5,column=0, ipadx=12, ipady = 5, padx=3, pady=5)
two = Button(root, text="2",bg="white", command=lambda: m1("2"))
two.grid(row=5,column=1, ipadx=12, ipady = 5, padx=3, pady=5)
three = Button(root, text="3",bg="white", command=lambda: m1("3"))
three.grid(row=5,column=2, ipadx=12, ipady = 5, padx=3, pady=5)

sub = Button(root, text="-",bg="lightgrey", command=lambda: m1("-"))
sub.grid(row=5,column=3, ipadx=15, ipady = 5, padx=3, pady=5)
equal = Button(root, text="=",bg="lightgrey", command=m3)
equal.grid(row=5,column=4, rowspan=2, ipadx=12, ipady = 32, padx=3, pady=5)

#row4
zero = Button(root, text="0",bg="white", command=lambda: m1("0"))
zero.grid(row=6,column=0,columnspan=2, ipadx=40, ipady = 5, padx=3, pady=5)
dot = Button(root, text=".",bg="lightgrey", command=lambda: m1("."))
dot.grid(row=6,column=2, ipadx=16, ipady = 5, padx=3, pady=5)
plus = Button(root, text="+",bg="lightgrey", command=lambda: m1("+"))
plus.grid(row=6,column=3, ipadx=12, ipady = 5, padx=3, pady=5)

#loop
root.mainloop()