from tkinter import *
import tkinter as tk
from tkinter import ttk
from tokenize import String
import datetime as date
from pyparsing import col


root =Tk()
root.title("Tab Widget")
root.geometry('770x450')

class items:
  def __init__(self, xps, xpm, ckint):
      self.xps = xps
      self.xpm = xpm
      self.ckint = ckint
      
  def xps1(self):
    return self.xps
  def xpm1(self):
    return self.xpm
  def ckint1(self):
    return self.ckint

def teste():
  chef = var_teste.get()
  if chef != 0:
    p1 = items(0.01,0.01,0.1)
    return p1
  else:
    p2 = items(1,1,1)
    return p2


var_teste = IntVar()
teste_resp = Checkbutton(root,variable=var_teste, onvalue=1, offvalue=0, command=teste)
teste_resp.pack()
teste_resp.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

def teste2():
  xps2 = teste().xps1()
  xpm2 = teste().xpm1()
  ckint2 = teste().ckint1()
  print(xps2,xpm2,ckint2)
  return xps2,xpm2,ckint2

but = Button(root, text='TESTE', command=teste2)
but.grid(column=0, row=1)

root.mainloop()