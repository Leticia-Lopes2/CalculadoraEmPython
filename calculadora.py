#IMPORTANDO A BIBLIOTECA TKINTER
from tkinter import *
from tkinter import ttk

#CORES
cor1 = "#3b3b3b" #BLACK 
cor2 = "#feffff" #WHITE
cor3 = "#38576b" #BLUE
cor4 = "#ECEFF1" #GREEN
cor5 = "#FFAB40" #ORANGE

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x304") 
janela.config(bg=cor1)


#TELA
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)


#CORPO
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


#VARIAVEL TODOS VALORES
todos_valores = ''


#FUNÇÂO
def  valor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

#PASSANDO VALOR PARA A TELA
    valor_texto.set(todos_valores)


#FUNÇÃO PARA CALCULAR
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


#FUNÇÃO LIMPAR A TELA
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


#LABEL
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#BOTÕES
b_1 = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command = lambda: valor('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo,command = lambda: valor('/'), text="/", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)


#LINHA 2
b_4 = Button(frame_corpo,command = lambda: valor('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=50)

b_5 = Button(frame_corpo,command = lambda: valor('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=50)

b_6 = Button(frame_corpo,command = lambda: valor('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=50)

b_7 = Button(frame_corpo,command = lambda: valor('*'), text="*", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=50)


#LINHA 3
b_4 = Button(frame_corpo, command = lambda: valor('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=100)
b_5 = Button(frame_corpo, command = lambda: valor('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=100)

b_6 = Button(frame_corpo, command = lambda: valor('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=100)

b_7 = Button(frame_corpo, command = lambda: valor('-'), text="-", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=100)


#LINHA 4
b_4 = Button(frame_corpo, command = lambda: valor('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=150)

b_5 = Button(frame_corpo, command = lambda: valor('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=150)

b_6 = Button(frame_corpo, command = lambda: valor('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=150)
 
b_7 = Button(frame_corpo, command = lambda: valor('+'), text="+", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=150)


#LINHA 5
b_1 = Button(frame_corpo, command = lambda: valor('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=201)

b_2 = Button(frame_corpo, command = lambda: valor('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=201)

b_3 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=201)

janela.mainloop()

#LMoura