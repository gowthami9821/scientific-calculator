import math 
from math import sin, cos, tan, pi, log10 , sqrt, log
from tkinter import *
#from PIL import Image, ImageTk
import sympy as sp

 

class calculator():
    def __init__(self):
        self.root = Tk()
        self.root.title("Scientific Calculator")
        self.root.geometry("356x402")
        self.root.minsize(356,402)
        self.root.maxsize(356,402)
        # self.root.resizable(1,1)
        self.root.config(bg = "white")
        self.value = StringVar()
        self.e = Entry(self.root,justify= RIGHT ,borderwidth= 2, relief= GROOVE,bg='sky Blue')
        self.e.grid(row = 0, column = 0, columnspan = 5,padx = 5,pady = 5)
        self.e.config(font=("Arial",19))
        self.e.focus_set()
        #tracks the deg and rad
        self.mode = StringVar(value = "deg") 

        #buttons
        #row_1
        self.button_sqrt = Button(self.root, text= "√",width = 5,command= lambda: self.insert_val('√('))
        self.button_sqrt.grid(row= 1, column= 0,padx= 2, pady= 2)
        self.button_sqrt.config(font=("Comic Sans MS",14))

        self.button_x_pow_n = Button(self.root, text= "x^n",width = 5,command= lambda: self.insert_val('^'))
        self.button_x_pow_n.grid(row= 1, column= 1,padx= 2, pady= 2)
        self.button_x_pow_n.config(font=("Comic Sans MS",14))
    
        self.button_inverse= Button(self.root, text= "1/x",width = 5,command= lambda: self.insert_val('1/'))
        self.button_inverse.grid(row=1, column= 2,padx= 4,pady= 4)
        self.button_inverse.config(font=("Comic Sans MS",14))
    
        self.button_xfacto = Button(self.root, text= "x!",width = 5,command= lambda: self.factorial())
        self.button_xfacto.grid(row= 1, column=3,padx= 2, pady= 2)
        self.button_xfacto.config(font=("Comic Sans MS",14))

        self.button_mod= Button(self.root, text= "mod",width = 5,command= lambda: self.insert_val('%'))
        self.button_mod.grid(row= 1, column= 4,padx= 2, pady= 2)
        self.button_mod.config(font=("Comic Sans MS",14))

        #row_2
        self.button_sin= Button(self.root, text= "sin",width = 5,command= lambda: self.eval_sine())
        self.button_sin.grid(row= 2, column= 0,padx= 2, pady= 2)
        self.button_sin.config(font=("Comic Sans MS",14))

        self.button_cos= Button(self.root, text= "cos",width = 5,command= lambda: self.eval_cos())
        self.button_cos.grid(row= 2, column= 1,padx= 2, pady= 2)
        self.button_cos.config(font=("Comic Sans MS",14))

        self.button_tan= Button(self.root, text= "tan",width = 5,command= lambda: self.eval_tan())
        self.button_tan.grid(row= 2, column= 2,padx= 2, pady= 2)
        self.button_tan.config(font=("Comic Sans MS",14))

        self.button_log = Button(self.root, text= "log",width = 5,command= lambda: self.insert_val('log('))
        self.button_log.grid(row= 3, column= 0,padx= 2, pady= 2)
        self.button_log.config(font=("Comic Sans MS",14))

        self.button_ln= Button(self.root, text= "ln",width = 5,command= lambda: self.insert_val('ln('))
        self.button_ln.grid(row= 3, column= 1,padx= 2, pady= 2)
        self.button_ln.config(font=("Comic Sans MS",14))

        #row_3
        self.button_cot= Button(self.root, text= "cot",width = 5,command= lambda: self.eval_cot())
        self.button_cot.grid(row= 2, column= 3,padx= 2, pady= 2)
        self.button_cot.config(font=("Comic Sans MS",14))

        self.button_pie= Button(self.root, text= "π",width = 5,command= lambda: self.insert_val(str(math.pi)))
        self.button_pie.grid(row= 3, column= 2,padx= 2, pady= 2)
        self.button_pie.config(font=("Comic Sans MS",14))

        self.button_mode= Button(self.root, text= "deg",width = 5,command= lambda: self.switch_mode())
        self.button_mode.grid(row= 2, column= 4,padx= 2, pady= 2)
        self.button_mode.config(font=("Comic Sans MS",14))

        self.button_open= Button(self.root, text= "(",width = 5,command= lambda: self.insert_val('('))
        self.button_open.grid(row= 3, column= 3,padx= 2, pady= 2)
        self.button_open.config(font=("Comic Sans MS",14))

        self.button_close= Button(self.root, text= ")",width = 5,command= lambda: self.insert_val(')'))
        self.button_close.grid(row= 3, column= 4,padx= 2, pady= 2)
        self.button_close.config(font=("Comic Sans MS",14))

        #row_4
        self.button_7= Button(self.root, text= "7",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('7'))
        self.button_7.grid(row= 4, column= 0,padx= 4, pady= 4)
        self.button_7.config(font=("Comic Sans MS",14))

        self.button_8= Button(self.root, text= "8",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('8'))
        self.button_8.grid(row= 4, column= 1,padx= 4, pady= 4)
        self.button_8.config(font=("Comic Sans MS",14))

        self.button_9= Button(self.root, text= "9",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('9'))
        self.button_9.grid(row= 4, column= 2,padx= 4, pady= 4)
        self.button_9.config(font=("Comic Sans MS",14))

        self.button_del= Button(self.root, text= "DEL",width = 5,bg='Orange',command= lambda: self.delete_val())
        self.button_del.grid(row= 4, column= 3,padx= 1, pady= 1)
        self.button_del.config(font=("Comic Sans MS",14))

        self.button_AC= Button(self.root, text= "AC",width = 5,bg='Orange',command=lambda: self.AC())
        self.button_AC.grid(row= 4, column= 4,padx= 1, pady= 1)
        self.button_AC.config(font=("Comic Sans MS",14))

        #row_5
        self.button_4= Button(self.root, text= "4",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('4'))
        self.button_4.grid(row= 5, column= 0,padx= 2, pady= 2)
        self.button_4.config(font=("Comic Sans MS",14))

        self.button_5= Button(self.root, text= "5",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('5'))
        self.button_5.grid(row= 5, column= 1,padx= 2, pady= 2)
        self.button_5.config(font=("Comic Sans MS",14))

        self.button_6= Button(self.root, text= "6",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('6'))
        self.button_6.grid(row= 5, column= 2,padx= 2, pady= 2)
        self.button_6.config(font=("Comic Sans MS",14))

        self.button_mul = Button(self.root, text= "*",width = 5,command= lambda: self.insert_val('*'))
        self.button_mul.grid(row= 5, column= 3,padx= 2, pady= 2)
        self.button_mul.config(font=("Comic Sans MS",14))

        self.button_div = Button(self.root, text= "/",width = 5,command= lambda: self.insert_val('/'))
        self.button_div.grid(row= 5, column= 4,padx= 2, pady= 2)
        self.button_div.config(font=("Comic Sans MS",14))

        #row_6
        self.button_1= Button(self.root, text= "1",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('1'))
        self.button_1.grid(row= 6, column= 0,padx= 2, pady= 2)
        self.button_1.config(font=("Comic Sans MS",14))

        self.button_2= Button(self.root, text= "2",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('2'))
        self.button_2.grid(row= 6, column= 1,padx= 2, pady= 2)
        self.button_2.config(font=("Comic Sans MS",14))

        self.button_3= Button(self.root, text= "3",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('3'))
        self.button_3.grid(row= 6, column= 2,padx= 2, pady= 2)
        self.button_3.config(font=("Comic Sans MS",14))

        self.button_add = Button(self.root, text= "+",width = 5,command= lambda: self.insert_val('+'))
        self.button_add.grid(row= 6, column= 3,padx= 2, pady= 2)
        self.button_add.config(font=("Comic Sans MS",14))

        self.button_sub = Button(self.root, text= "-",width = 5,command= lambda: self.insert_val('-'))
        self.button_sub.grid(row= 6, column= 4,padx= 2, pady= 2)
        self.button_sub.config(font=("Comic Sans MS",14))

        #row_7
        self.button_e= Button(self.root, text= "e",width = 5,command= lambda: self.insert_val('e'))
        self.button_e.grid(row= 7, column= 0,padx= 2, pady= 2)
        self.button_e.config(font=("Comic Sans MS",14))

        self.button_0= Button(self.root, text= "0",width = 5,bg= 'lightgreen',command= lambda: self.insert_val('0'))
        self.button_0.grid(row= 7, column= 1,padx= 2, pady= 2)
        self.button_0.config(font=("Comic Sans MS",14))

        self.button_dot= Button(self.root, text= ".",width = 5,command= lambda: self.insert_val('.'))
        self.button_dot.grid(row= 7, column= 2,padx= 2, pady= 2)
        self.button_dot.config(font=("Comic Sans MS",14))

        self.button_equals = Button(self.root, text= "=",width = 11,bg='light yellow',command=lambda:self.calculate())
        self.button_equals.grid(row= 7, column= 3,columnspan= 2,padx= 2, pady= 2)
        self.button_equals.config(font=("Comic Sans MS",14))

        
        #icon = ImageTk.PhotoImage(file = r'C:\Users\neeso\OneDrive\文件\cal\icon_of_cal.png')
        #self.root.iconphoto(True,icon)

        self.root.mainloop()

    #func to insert into entry
    def insert_val(self, val):
        self.e.insert(END, val)

    #func to delete the last value   
    def delete_val(self):
        x = self.e.get()
        self.e.delete(0,'end')
        y = x[:-1]
        self.e.insert(0,y)  

    #func to clear all      
    def AC(self):
        self.e.delete(0,'end')

    #func to evaluate the expression
    def calculate(self):
        x = self.e.get().strip()
        if '^' in x:
                base_str, exponent_str = x.split('^')
                if base_str and exponent_str:
                    if base_str == 'e':
                        convert_e = 2.71828182
                        y = float(exponent_str)
                        res = convert_e ** y
                        self.e.delete(0, 'end')
                        self.e.insert(0, res)
                        return 
                    else:
                        x = float(base_str)
                        y = float(exponent_str)
                        res = x ** y
                        self.e.delete(0, 'end')
                        self.e.insert(0, res)
                        return 
        elif 'log(' in x:
            try:
                base_str = x.split('log(')[1].split(')')[0]
                base = float(base_str)
                res = math.log10(base)
                self.e.delete(0, 'end')
                self.e.insert(0, res)
                return
            except ValueError:
                self.e.delete(0, 'end')
                self.e.insert(0, "Error")
                return
        elif 'ln(' in x:
            try:
                base_str = x.split('ln(')[1].split(')')[0]
                base = float(base_str)
                res = math.log(base)
                self.e.delete(0, 'end')
                self.e.insert(0, res)
                return
            except ValueError:
                self.e.delete(0, 'end')
                self.e.insert(0, "Error")
                return
        elif '√(' in x:
            try:
                base_str = x.split('√(')[1].split(')')[0]
                base = float(base_str)
                res = math.sqrt(base)
                self.e.delete(0, 'end')
                self.e.insert(0, res)
                return
            except ValueError:
                self.e.delete(0, 'end')
                self.e.insert(0, "Error")
                return
        elif 'e' in x:
            e = math.e
            ans = float(eval(x))
            self.e.delete(0,'end')
            self.e.insert(0,ans)
        try:
            ans = float(eval(x))
            self.e.delete(0,'end')
            self.e.insert(0,ans)
        except Exception as error:
            self.e.delete(0,'end')
            self.e.insert(0, "Invalid input")
    
    #func to evaluate factorial
    def factorial(self):
        try:
            n = int(self.e.get())
            result = sp.factorial(n)
            self.e.delete(0, 'end')
            self.e.insert(0, result)
        except Exception as e:
            self.e.delete(0, 'end')
            self.e.insert(0, "Error")

    #func to evaluate trignometric expressions in radians
    def eval_sine(self):
        try:
            cal = self.e.get()
            angle = float(cal)
            if self.mode.get() == "deg":
                angle = math.radians(angle)
            res = math.sin(angle)
            if abs(res) < 1e-10:
                res = 0.0
            res = round(res, 5)
            self.e.delete(0, 'end')
            self.e.insert(0, str(res))
        except Exception as e:
            self.e.delete(0, 'end')
            self.e.insert(0, "Error")

    def eval_cos(self):
        try:
            cal = self.e.get()
            angle = float(cal)
            if self.mode.get() == "deg":
                angle = math.radians(angle)
            res = math.cos(angle)
            res = cos((float(cal)))
            if abs(res) < 1e-10:
                res = 0.0
            res = round(res, 5)
            self.e.delete(0, 'end')
            self.e.insert(0, str(res))

        except Exception as e:
            self.e.delete(0, 'end')
            self.e.insert(0, "Error")
    
    def eval_tan(self):
        try:
            cal = self.e.get()
            angle = float(cal)
            if self.mode.get() == "deg":
                angle = math.radians(angle)
            res = math.tan(angle)
            res = tan((float(cal)))
            # Set a threshold for rounding to zero
            if abs(res) < 1e-10:
                res = 0.0
            res = round(res, 5)
            self.e.delete(0, 'end')
            self.e.insert(0, str(res))
        except Exception as e:
            self.e.delete(0, 'end')
            self.e.insert(0, "Error")

    def eval_cot(self):
        try:
            cal = self.e.get()
            angle = float(cal)
            if self.mode.get() == "deg":
                angle = math.radians(angle)
            if math.isclose(math.tan(angle), 0, abs_tol = 1e-10):
                self.e.delete(0, "end")
                self.e.insert(0, "Cannot divide by zero")
                return 
            res = 1/math.tan(angle)
            res = round(res, 5)
            self.e.delete(0, 'end')
            self.e.insert(0, str(res))
        except Exception as e:
            self.e.delete(0, 'end')
            self.e.insert(0, "Error")
    
    def switch_mode(self):
        if self.mode.get() == "deg":
            self.mode.set("rad")
            self.button_mode.config(text = "rad")
        else:
            self.mode.set("deg")
            self.button_mode.config(text = "deg")
           
# main function          
if __name__ == "__main__":
    calculator()
    
