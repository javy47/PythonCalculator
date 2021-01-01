from tkinter import *
from calculator import Calculator
import time

root = Tk()
root.title('Calculator')
root.config(bg='#DDDDDD')



e = Entry(root,font=('default',20), justify='right', width=20,bg='red', highlightthickness=0, bd=0)
e.grid(row=0,column=0, columnspan=3,padx=5,pady=2,ipady=10)
e.config(highlightbackground= '#DDDDDD', highlightcolor='#DDDDDD')
e.insert(0,'0')

#Organizing the Placing of buttons
# pad = Entry(root, width=20,bg='red', highlightthickness=0, bd=0)
# pad.config(highlightbackground= '#DDDDDD', highlightcolor='#DDDDDD')
# pad.grid(row=0,column=3)

last_number = ' '

#This represents the Clear Everything button on the Graphical UI
def button_clear():
    e.delete(0,END)
    e.insert(0,'0')
    last_number =' '
    Button_dot['state'] = 'normal'
    Button_add['state'] = 'normal'
    Button_sub['state'] = 'normal'
    Button_mul['state'] = 'normal'
    Button_div['state'] = 'normal'

#Limits the User to only 1 decimal button per number
def button_state():
    Button_dot['state'] = 'disabled'


#Takes input from the number buttons and the equal button  
def button_click(button):
    if button == '=':
        # last_number = e.get()
        # print(last_number)
        button_equal()
        return

    
    #if the user pressed the '.' button they will be prevnted from pressing it again until the dot is removed or a new number is entered
    if button == '.':
        button_state()
  
    #Removing the error message from the screen while keeping the new values a user enters
    if 'YOU CAN NOT DIVIDE BY 0!' in e.get():
        txt = e.get()
        current = txt.split('!')[1]
        e.delete(0,END)
        e.insert(0,str(current))
   
      
    current= e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(button))
   
    

def button_add():
    Button_dot['state'] = 'normal'

    if e.get() != '':
        first_number = e.get()
        test_value(first_number)
    global math
    math = '+'
    

def button_subtract():
    Button_dot['state'] = 'normal'
   
    if e.get() != '':
        first_number = e.get()
        test_value(first_number)
    global math
    math = '-'
    

def button_divide():
    Button_dot['state'] = 'normal'
    
    if e.get() != '':
        first_number = e.get()
        test_value(first_number)
    global math
    math = '/'
    

def button_multiply():
    Button_dot['state'] = 'normal'
    
    if e.get() != '':
        first_number = e.get()
        test_value(first_number)
    global math
    math = '*'
    
    
def test_value(num1):
    global first_num
    try:
        first_num = int(num1)
        e.delete(0,END)
    except ValueError:
        first_num = float(num1)
        e.delete(0,END)


def button_equal():
    second_number = e.get()
    print(second_number)
    e.delete(0,END)

    if math == '+':
        try:
            e.insert(0, first_num + int(second_number))
            last_number = e.get()
        except ValueError:
             e.insert(0, first_num + float(second_number))
             last_number = e.get()
    if math == '-':
        try:
            e.insert(0, first_num - int(second_number))
            last_number = e.get()
        except ValueError:
            e.insert(0, first_num - float(second_number))
            last_number = e.get()
    if math == '/':
        try:
            e.insert(0, first_num / int(second_number))
            last_number = e.get()
        except ValueError:
            e.insert(0, first_num / float(second_number))
            last_number = e.get()
        except ZeroDivisionError:
            e.insert(0, 'YOU CAN NOT DIVIDE BY 0!')
            
    if math == '*':
        try:
            e.insert(0, first_num * int(second_number))
            last_number = e.get()
        except ValueError:
            e.insert(0, first_num * float(second_number))
            last_number = e.get()
   

#Defining the Buttons
Button_0 = Button(root, text="0", padx=40,pady=20,  command= lambda: button_click(0))
Button_1 = Button(root, text="1",padx=40,pady=20,bg='#EBEBEB', bd=0, command=lambda: button_click(1))
Button_2 = Button(root, text="2",padx=40,pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text="3",padx=40,pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text="4",padx=40,pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text="5",padx=40,pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text="6",padx=40,pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text="7",padx=40,pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text="8",padx=40,pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text="9",padx=40,pady=20, command=lambda: button_click(9))

#Defining the operation buttons
Button_neg = Button(root, text="+/-",padx=34,pady=20, command=lambda: button_click('+/-'))
Button_dot = Button(root, text=".",padx=41,pady=20,state='normal',command=lambda: button_click('.'))

Button_add = Button(root, text="+",padx=40,pady=20,state= 'normal', command= button_add)
Button_sub = Button(root, text="-",padx=41,pady=20,state= 'normal', command= button_subtract)
Button_mul = Button(root, text="x",padx=40,pady=20,state= 'normal', command=button_multiply)
Button_div = Button(root, text="÷",padx=40,pady=20,state= 'normal', command= button_divide)
Button_equal = Button(root,text='=',padx=40, pady=20, command=lambda: button_click('='))

#Defining Buttons For erasing data
Button_clearall = Button(root,text='CE',padx=36, pady=20, command=button_clear)


#Placing the button in the order they appear on most calculators
Button_1.grid(row=4,column=0)
Button_2.grid(row=4,column=1)
Button_3.grid(row=4,column=2)

Button_4.grid(row=3,column=0)
Button_5.grid(row=3,column=1)
Button_6.grid(row=3,column=2)

Button_7.grid(row=2,column=0)
Button_8.grid(row=2,column=1)
Button_9.grid(row=2,column=2)

# Button_neg.grid(row=5,column=0)
Button_0.grid(row=5,column=1)
Button_dot.grid(row=5,column=2)

#Placing Operation Buttons
Button_sub.grid(row=3,column=3)
Button_add.grid(row=4,column=3)
Button_mul.grid(row=2,column=3)
Button_div.grid(row=0,column=3)
Button_equal.grid(row=5,column=3)

#Placing Buttons for deleting data row should be 6 when i inplement  the+/- option
Button_clearall.grid(row=5,column=0)


root.mainloop()