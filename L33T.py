from tkinter import *

root=Tk()
root.title('L33t')

def traduzir():
	lista=list(entrada.get().upper())
	for i in range(len(lista)):
		if lista[i]=='O':
			lista[i]='0'
		elif lista[i]=='L':
			lista[i]='1'
		elif lista[i]=='E':
			lista[i]='3'
		elif lista[i]=='A':
			lista[i]='4'
		elif lista[i]=='T':
			lista[i]='7'
		else:
			continue
	resultado.delete(0,END)
	resultado.insert(0,''.join(lista))


frame_entrada=LabelFrame(root,text='Entrada')
frame_saída=LabelFrame(root, text='Resultado')
entrada = Entry(frame_entrada)
botao = Button(root, text='Traduzir', command=traduzir)
resultado = Entry(frame_saída)

frame_entrada.pack()
entrada.pack()
botao.pack()
frame_saída.pack()
resultado.pack()


root.mainloop()
