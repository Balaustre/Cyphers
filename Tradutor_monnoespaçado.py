from tkinter import *
from tkinter import messagebox
import pyperclip

root = Tk()
root.title('Monoespaçado')

def copiar():
	if resultado.get() != '':
		pyperclip.copy(resultado.get())
		messagebox.showinfo(title='Concluído', message='Texto copiado para a área de transferência.')
		print(var)
	else:
		messagebox.showerror(title='Erro', message='Não há o que ser copiado.')

def traduzir():
	global var
	var = ''
	trad =texto.get()
	for i in range(len(trad)):
		var=var+trad[i]+' '
	resultado.delete(0,END)
	resultado.insert(0,var)

frame_entrada = LabelFrame(root, text='Entrada')
frame_saída = LabelFrame(root, text='Resultado')



texto= Entry(frame_entrada)
botão_traduzir=Button(root, text='Traduzir', command=traduzir)
resultado = Entry(frame_saída)
botão_copiar = Button(frame_saída, text='Copiar', command=copiar)

frame_entrada.pack()
texto.pack()
botão_traduzir.pack()
frame_saída.pack()
resultado.pack()
botão_copiar.pack()


root.mainloop()
