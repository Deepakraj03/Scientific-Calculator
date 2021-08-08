from tkinter import *
import math


root = Tk()
root.geometry("550x568+0+0")
root.title("Scientific Calculator - Deepakraj ")

expression = ""

#--Functions for calculation
def press(n):
   global expression
   expression = expression + str(n)
   data.set(expression)
def equalpress():
   try:
       global expression
       total = str(eval(expression))
       data.set(total)
       expression = total + ""
   except:
       data.set("Math error")
       error=""
def clear():
   global expression
   expression=""
   data.set("")
def pi():
   try:
      global expression
      expression = str(math.pi)
      data.set(expression)
   except:
      data.set("Math error")
      error=""
def sqrt():
   try:
      global expression
      expression = math.sqrt(eval(expression))
      data.set(expression)
   except:
      data.set("Math error")
      error=""
def sin():
   global expression
   try:
      expression = float(disp.get())
      expression = math.sin(math.radians(expression))
      data.set(str(expression))
   except:
      data.set("Math error")
      error=""
def cos():
   global expression
   try:
      expression = float(disp.get())
      expression = math.cos(math.radians(expression))
      data.set(str(expression))
   except:
      data.set("Math error")
      error=""
def tan():
   global expression
   try:
      expression = float(disp.get())
      expression = math.tan(math.radians(expression))
      data.set(str(expression))
   except:
      data.set("Math error")
      error=""
def exp():
   global expression
   try:
      expression = str(math.e)
      data.set(expression)
   except:
      data.set("Math error")
      error=""
def log():
   global expression
   try:
      expression = float(disp.get())
      expression = math.log10(expression)
      data.set(expression)
   except:
      data.set("Math error")
      error=""
def asin():
   global expression
   try:
      expression = float(disp.get())
      expression = math.degrees(math.asin(expression))
      data.set(str(expression))
   except:
      data.set("Math error")
      error=""
def acos():
   global expression
   try:
      expression = float(disp.get())
      expression = math.degrees(math.acos(expression))
      data.set(str(expression))
   except:
      data.set("Math error")
      error=""
def atan():
   global expression
   try:
      expression = float(disp.get())
      expression = math.degrees(math.atan(expression))
      data.set(str(expression))
   except:
      data.set("Math error")
      error=""

def fact():
   global expression
   try:
      expression = int(disp.get())
      expression = math.factorial(expression)
      data.set(expression)
   except:
      data.set(expression)
      error=""


#--Display
data = StringVar()
disp = Entry(root, font="arial 20", fg="black", bg="#87CEFA", relief = SUNKEN, justify=RIGHT, insertbackground="black", cursor="arrow", textvariable = data)
disp.bind("<Return>", equalpress)
disp.focus_set()
disp.pack(expand = True, fill= BOTH)

#--Buttons
row1 = Frame(root)
row1.pack(expand=True, fill=BOTH)

btn7 = Button(row1, text="7", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(7))
btn8 = Button(row1, text="8", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(8))
btn9 = Button(row1, text="9", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(9))
clr =  Button(row1, text="AC", font = ('arial 20'), command=clear,height=1,width=14, bd = 4, fg = "RED" )


row2 = Frame(root)
row2.pack(expand=TRUE, fill=BOTH)

btn4 = Button(row2, text="4", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(4))
btn5 = Button(row2, text="5", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(5))
btn6 = Button(row2, text="6", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(6))
plus = Button(row2, text="+", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press("+"))
minus = Button(row2, text="-", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press("-"))

row3 = Frame(root)
row3.pack(expand=TRUE, fill= BOTH)

btn1 = Button(row3, text="1", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(1))
btn2 = Button(row3, text="2", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(2))
btn3 = Button(row3, text="3", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(3))
multiply = Button(row3, text="x", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press("*"))
divide = Button(row3, text="/", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press("/"))

row4 = Frame(root)
row4.pack(expand=TRUE, fill= BOTH)

btn0 = Button(row4, text="0", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press(0))
btndot = Button(row4, text="•", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press("."))
btnpi = Button(row4, text="π", font = ('arial 20'), height=1,width=6, bd = 4, command=pi)
btne = Button(row4, text="e", font = ('arial 20'), height=1,width=6, bd = 4, command=exp)
equal = Button(row4, text="=", font = ('arial 20'), height=1,width=6, bd = 4, command=equalpress)

row5 = Frame(root)
row5.pack(expand=TRUE, fill= BOTH)

sqrt = Button(row5, text="Sqrt", font = ('arial 20'), height=1,width=6, bd = 4, command=sqrt)
btnsin = Button(row5, text="SIN", font = ('arial 20'), height=1,width=6, bd = 4, command=sin)
btncos = Button(row5, text="COS", font = ('arial 20'), height=1,width=6, bd = 4, command=cos)
btntan = Button(row5, text="TAN", font = ('arial 20'), height=1,width=6, bd = 4, command=tan)
btnpow = Button(row5, text="x^y", font = ('arial 20'), height=1,width=6, bd = 4, command=lambda: press("**"))

row6 = Frame(root)
row6.pack(expand=TRUE, fill= BOTH)

btnlog = Button(row6, text ="log", font = ('arial 20'), height=1,width=6, bd = 4, command=log)
btnasin = Button(row6, text ="sin-1", font = ('arial 20'), height=1,width=6, bd = 4, command=asin)
btnacos = Button(row6, text ="Cos-1", font = ('arial 20'), height=1,width=6, bd = 4, command=acos)
btnatan = Button(row6, text ="Tan-1", font = ('arial 20'), height=1,width=6, bd = 4, command=atan)
btnfact = Button(row6, text ="n!", font = ('arial 20'), height=1,width=6, bd = 4, command=fact)

btn7.pack(side= LEFT, expand=True, fill= BOTH)
btn8.pack(side= LEFT, expand=True, fill= BOTH)
btn9.pack(side= LEFT, expand=True, fill= BOTH)
clr.pack(side= LEFT, expand=True, fill= BOTH)

btn4.pack(side= LEFT, expand=True, fill= BOTH)
btn5.pack(side= LEFT, expand=True, fill= BOTH)
btn6.pack(side= LEFT, expand=True, fill= BOTH)
plus.pack(side= LEFT, expand=True, fill= BOTH)
minus.pack(side= LEFT, expand=True, fill= BOTH)

btn1.pack(side= LEFT, expand=True, fill= BOTH)
btn2.pack(side= LEFT, expand=True, fill= BOTH)
btn3.pack(side= LEFT, expand=True, fill= BOTH)
multiply.pack(side= LEFT, expand=True, fill= BOTH)
divide.pack(side= LEFT, expand=True, fill= BOTH)

btn0.pack(side= LEFT, expand=True, fill= BOTH)
btndot.pack(side= LEFT, expand=True, fill= BOTH)
btnpi.pack(side= LEFT, expand=True, fill= BOTH)
btne.pack(side = LEFT, expand=True, fill = BOTH)
equal.pack(side= LEFT, expand=True, fill= BOTH)

sqrt.pack(side= LEFT, expand=True, fill= BOTH)
btnsin.pack(side= LEFT, expand=True, fill= BOTH)
btncos.pack(side= LEFT, expand=True, fill= BOTH)
btntan.pack(side= LEFT, expand=True, fill= BOTH)
btnpow.pack(side= LEFT, expand=True, fill= BOTH)

btnlog.pack(side= LEFT, expand=True, fill= BOTH)
btnasin.pack(side= LEFT, expand=True, fill= BOTH)
btnacos.pack(side= LEFT, expand=True, fill= BOTH)
btnatan.pack(side= LEFT, expand=True, fill= BOTH)
btnfact.pack(side= LEFT, expand=True, fill= BOTH)

root.mainloop()
