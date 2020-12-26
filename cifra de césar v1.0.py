from tkinter import *
root= Tk()
root.title('Ceasar Translator')
root.geometry('200x250')
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
valor = 0

def posicao_reversa(posição, cifra):
    nova_posição = (posição - cifra)%26
    return nova_posição

def posicao(posição, cifra):
    nova_posição = (posição + cifra)%26
    return nova_posição

def Resultado():
    cifra = slider.get()
    global alfabeto
    mensagem = texto.get()
    mensagem_criptografada = ''
    for letra in mensagem:
        if letra == ' ':
            mensagem_criptografada+=' '
        else:
            posição = alfabeto.find(letra)
            if valor == 0:
                nova_posição = posicao(posição, cifra)
                print('está criptografando')
            else:
                nova_posição = posicao_reversa(posição, cifra)
                print('está descriptografando')
            mensagem_criptografada += alfabeto[nova_posição]
    resultado.delete(0, END)
    resultado.insert(0, mensagem_criptografada)



criptografar = IntVar()
def radio1():
    global valor
    valor = 0
def radio2():
    global valor
    valor = 1



opcao = LabelFrame(root, text = 'Opção')
cripto = Radiobutton(opcao, text = 'Criptografar', variable = criptografar, value = 0, command = radio1)
descripto = Radiobutton(opcao, text = 'Descriptografar', variable = criptografar, value = 1, command = radio2)
num_cifra = LabelFrame(root, text = 'Cifra')
Entrada = LabelFrame(root, text='Entrada')
texto= Entry(Entrada)
saída=LabelFrame(root, text='Resultado')
botao=Button(root, text='Converter', command=Resultado)
slider=Scale(num_cifra, from_=1, to=26, orient=HORIZONTAL)
resultado=Entry(saída)

texto.pack()
Entrada.pack()
num_cifra.pack()
slider.pack()
opcao.pack()
cripto.pack(anchor = W)
descripto.pack(anchor = W)
botao.pack()
saída.pack()
resultado.pack()
#Resultado('iy res uyivs iwxyhev jmwmge', 4, False)
    
mainloop()