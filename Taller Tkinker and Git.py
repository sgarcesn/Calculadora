import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import Menu
from tkinter import messagebox

def main():
    init_window()
        
def init_window():

    window=tk.Tk()
    window.title('Mi Primera Aplicación')
    window.geometry('420x220')

    label= tk.Label(window,text="Calculadora",font=("Arial Bold",15))
    label.grid(column=0,row=0)

    label_entrada1= tk.Label(window,text="Ingrese el primer numero",font=("Arial Bold",10))
    label_entrada1.grid(column=0,row=1)
    
    label_entrada2= tk.Label(window,text="Ingrese el segundo numero",font=("Arial Bold",10))
    label_entrada2.grid(column=0,row=2)
    
    entrada1=tk.Entry(window, width=10)
    entrada2=tk.Entry(window, width=10)
    
    entrada1.focus()
    entrada2.focus()
    
    entrada1.grid(column=1,row=1)
    entrada2.grid(column=1,row=2)

    label_operador= tk.Label(window,text="Escoja un operador",font=("Arial Bold",10))
    label_operador.grid(column=0,row=3)

    combo_operadores=ttk.Combobox(window)
    combo_operadores['values']=["+","-","*","/","pow"]
    combo_operadores.current(0)
    combo_operadores.grid(column=1,row=3)

    label_resultado= tk.Label(window,text="Resultado: ",font=("Arial Bold",15))
    label_resultado.grid(column=0,row=5)
    
    #Widget del botón
    boton = tk.Button(window,
                      command = lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get()),
                      text='Calcular',
                      bg="purple",
                      fg="white")
    
    boton.grid(column = 1, row =4)
    
    #Widget de progressbar
    style  = ttk.Style()
    style.theme_use("default")
    style.configure("purple.Horizontal.TProgressbar", background='purple')
    
    bar = Progressbar(window, length=220, style='purple.Horizontal.TProgressbar')
    bar['value']= 50
    bar.grid(column=0, row=6)
    
    #Widget de barra desplegable de menú con varios items
    menu = Menu (window)
    new_item = Menu (menu)
    new_item.add_command(label='Sencilla')
    
    new_item.add_separator()
    
    new_item.add_command(label='Cientifica (Todavía no está ;D)')
    menu.add_cascade(label='Tipo de Calculadora', menu=new_item)
    window.config(menu=menu)
    
    menu2 = Menu (window)
    menu2.add_command(label='Loquesea')
    window.config()
    
    messagebox.showinfo('Instrucciones para el uso', """Primero ingrese los numeros a operar
Luego escoja un operador a realizar
Despues clickee en el botón de calcular y le saldrá su resultado""")
    
    window.mainloop()
    
def calculadora(num1,num2,operador):
    if operador=="+":
        resultado = num1+num2
    elif operador == "-":
        resultado = num1-num2
    elif operador == "*":
        resultado = num1*num2
    elif operador == "/":
        resultado = round(num1/num2,2)
    else:
        resultado = num1**num2
    return resultado
     
def click_calcular(label1, num1, num2, operador):
    valor1=float(int(num1))
    valor2=float(int(num2))
    res=calculadora(valor1,valor2,operador)
    label1.configure(text = 'Resultado: ' + str(res))
    

#----------------------
 
main()