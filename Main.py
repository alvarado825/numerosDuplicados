from tkinter import *
from Functions import *

# Funções atribuidas aos botões abrir arquivos e comparar, faz a chamada das funções em function
def abrirArquivo():
    origemTxt.delete(0, 'end')
    abrirArquivoOrigem(origemTxt)
    
def abrirComparante():
    compTxt.delete(0, 'end')
    abrirArquivoComparante(compTxt)

def comparar():
    comparaAquivos(texto)
    
#interface gráfica
    
root = Tk()
root.resizable(0,0)
root.geometry('350x350')
root.title('Checar Números Repetidos')

frame =Frame(root)
frame.grid(pady = 30, padx = 10)


label = Label(frame, text = 'Arquivo Origem', justify = RIGHT)
label.place(x= 10, y = 25)
label.pack()

origemTxt = Entry(root)
origemTxt.place(x = 120, y = 30 )

abrirButton = Button(root, text = 'Abrir Arquivo',width = 10, height = 1,bd = 1, command = abrirArquivo)
abrirButton.place(x = 260, y = 29)
abrirButton.pack

frame1 =Frame(root)
frame1.grid(pady = 30, padx = 10)

label2 = Label(frame, text = 'Arquivo Destino', justify = RIGHT)
label2.place(x = 10, y = 200 )
label2.pack()

compTxt = Entry(root)
compTxt.place(x = 120, y = 60 )

abrirButton1 = Button(root, text = 'Abrir Arquivo',width = 10, height = 1,bd = 1, command = abrirComparante)
abrirButton1.place(x = 260, y = 58 )
abrirButton1.pack

comparaButton = Button(root, text = 'Comparar', width = 10, height = 1,bd = 1, command = comparar)
comparaButton.place(x = 150 , y = 85)
comparaButton.pack

texto = Text(root)
texto.place(x = 10, y = 115, width = 335, height = 230)

root.mainloop()







