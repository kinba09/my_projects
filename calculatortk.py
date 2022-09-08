from tkinter import *

win = Tk()
win.geometry("328x225")
win.resizable(0,0)
win.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
 
def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
 
expression = ""


input_text = StringVar()
input_field = Entry(win,text=input_text,width=54).grid(row=0,column=0,columnspan=4)

clear = Button(win,text='C',width=33,height=2, command= lambda : bt_clear()).grid(row=1,column=0,columnspan=3)
slash = Button(win,text='/',width=10,height=2, command= lambda : btn_click("/")).grid(row=1,column=3,columnspan=1)

seven = Button(win,text='7',width=10,height=2, command= lambda : btn_click("7")).grid(row=2,column=0)
eigth = Button(win,text='8',width=10,height=2, command= lambda : btn_click("8")).grid(row=2,column=1)
nine = Button(win,text='9',width=10,height=2, command= lambda : btn_click("9")).grid(row=2,column=2)
multi = Button(win,text='*',width=10,height=2,command= lambda : btn_click("*")).grid(row=2,column=3)

four = Button(win,text='4',width=10,height=2,command= lambda : btn_click("4")).grid(row=3,column=0)
five = Button(win,text='5',width=10,height=2,command= lambda : btn_click("5")).grid(row=3,column=1)
six = Button(win,text='6',width=10,height=2,command= lambda : btn_click("6")).grid(row=3,column=2)
plus = Button(win,text='+',width=10,height=2,command= lambda : btn_click("+")).grid(row=3,column=3)

one = Button(win,text='1',width=10,height=2,command= lambda : btn_click("1")).grid(row=4,column=0)
two = Button(win,text='2',width=10,height=2, command= lambda : btn_click("2")).grid(row=4,column=1)
three = Button(win,text='3',width=10,height=2, command= lambda : btn_click("3")).grid(row=4,column=2)
minus = Button(win,text='-',width=10,height=2, command= lambda : btn_click("-")).grid(row=4,column=3)

zero = Button(win,text='0',width=22,height=2, command= lambda : btn_click("0")).grid(row=5,column=0,columnspan=2)
dot = Button(win,text='.',width=10,height=2, command= lambda : btn_click(".")).grid(row=5,column=2)
eq = Button(win,text='=',width=10,height=2, command= lambda : bt_equal()).grid(row=5,column=3)


win.mainloop()