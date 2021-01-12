import tkinter.filedialog as FileDialog
import tkinter.messagebox as MsgBox

index = '0.0'

#Abre uma caixa de diálogo para o usuário escolher um arquivo txt, recebe um widget Entry como parametro, para mostrar o caminho do arquivo escolhido
def abrirArquivoOrigem(textbox):
    global arquivoOrigem
    arquivoOrigem = FileDialog.askopenfile(filetypes=[('Todos os Arquivos', '.*'), ('Arquivos de Texto', '.txt')]).name
    textbox.insert(0,arquivoOrigem)


#Abre uma caixa de diálogo para o usuário escolher um arquivo txt, recebe um widget Entry como parametro, para mostrar o caminho do arquivo escolhido
def abrirArquivoComparante(textbox):
    global arquivoComparante
    arquivoComparante = FileDialog.askopenfile(filetypes=[('Todos os Arquivos', '.*'), ('Arquivos de Texto', '.txt')]).name
    textbox.insert(0, arquivoComparante)
    

#Faz a comparação dos arquivos e retorna a quantidade de numeros repetidos e suas numeraçoes
def comparaAquivos(textbox):
    global arquivoOrigem
    global arquivoComparante
    global index
    dadosOrigem = []
    dadosComparante = []
    cont = 0
    
    textbox.delete('1.0', index)

    try:
        with open(arquivoOrigem, 'r') as arqOrigem:
            dadostemp = arqOrigem.readlines()

            for line in dadostemp:
                dadosOrigem.append(line.replace('\n', ''))

        with open(arquivoComparante, 'r') as arqComp:
            dadostemp = arqComp.readlines()

            for line in dadostemp:
                dadosComparante.append(line.replace('\n', ''))
    except:
        MsgBox.showerror('Escolha um Arquivo')

    for line in dadosOrigem:
        if line in dadosComparante:
            textbox.insert('1.0', line +'\n')
            cont += 1
    
    index = str(cont+3) + '.0'
    textbox.insert(index, '\nTotal de ' + str(cont)+ ' números repetidos')
    cont = 0
    arquivoOrigem = None
    arquivoComparante =  None
