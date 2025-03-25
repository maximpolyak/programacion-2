from tkinter import *

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.configure(background="#e4e4e4",borderwidth="20")

        self.i = 0
        
        self.textbox = Entry(ventana, font = ('Arial 20'), justify="right")
        self.textbox.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=10, ipady=10)

        btn1 = self.crearBtn(1,5,2,"click_btn")
        btn2 = self.crearBtn(2,5,2,"click_btn")
        btn3 = self.crearBtn(3,5,2,"click_btn")
        btn4 = self.crearBtn(4,5,2,"click_btn")
        btn5 = self.crearBtn(5,5,2,"click_btn")
        btn6 = self.crearBtn(6,5,2,"click_btn")
        btn7 = self.crearBtn(7,5,2,"click_btn")
        btn8 = self.crearBtn(8,5,2,"click_btn")
        btn9 = self.crearBtn(9,5,2,"click_btn")
        btn0 = self.crearBtn(0,13,2,"click_btn")
        btn_par1 = self.crearBtn("(",5,2,"click_btn")
        btn_par2 = self.crearBtn(")",5,2,"click_btn")
        btn_sum = self.crearBtn("+",5,2,"click_btn")
        btn_res = self.crearBtn("-",5,2,"click_btn")
        btn_mul = self.crearBtn("*",5,2,"click_btn")
        btn_div = self.crearBtn("/",5,2,"click_btn")
        btn_dec = self.crearBtn(".",5,2,"click_btn")
        btn_igu = self.crearBtn("=",5,2,"click_operar")
        btn_borr = self.crearBtn("C",5,2,"click_borrar")

        list_btn_or = [
            btn_borr, btn_par1, btn_par2, btn_sum,
            btn1, btn2, btn3, btn_res,
            btn4, btn5, btn6, btn_mul,
            btn7, btn8, btn9, btn_div,
            btn0, btn_dec, btn_igu
        ]

        contador=0
        for fila in range(1,5):
            for columna in range(4):
                list_btn_or[contador].grid(row=fila,column=columna, padx=2, pady=6)
                contador += 1
                #la última línea tiene sólo 3 btns
            fila += 1
        for columna in range(3):
            if columna == 0:
                list_btn_or[contador].grid(row=fila,column=columna, columnspan=2, padx=2, pady=6)
            else:
                list_btn_or[contador].grid(row=fila,column=columna+1, padx=2, pady=6)
            contador += 1
        return
    
    def crearBtn(self, val, wd, hg, cmmclick):
        if cmmclick == "click_borrar":
            it_btn = Button(self.ventana, text=val, width=wd, height=hg, font="Arial 15", command = lambda:self.click_borrar())
        elif cmmclick == "click_operar":
            it_btn = Button(self.ventana, text=val, width=wd, height=hg, font="Arial 15", command = lambda:self.click_operar())
        else:
            it_btn = Button(self.ventana, text=val, width=wd, height=hg, font="Arial 15", command = lambda:self.click_btn(val))
        
        return it_btn
    
    #funciones calculadora
    def click_btn(self,valor):
        self.textbox.insert(self.i, valor)
        self.i += 1
    def click_borrar(self):
        self.textbox.delete(0, END)
        self.i = 0
    def click_operar(self):
        ecuacion = self.textbox.get()
        resultado = eval(ecuacion)
        #print(ecuacion)
        #print(resultado)
        self.textbox.delete(0, END)
        self.textbox.insert(0, resultado)
        self.i = len(str(resultado))+1
    
ventana = Tk()
calculadora = Interfaz(ventana)

ventana.mainloop()