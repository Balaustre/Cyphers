mensagem = input('mensagem a descriptografar: ')
cifra = int(input('cifra: '))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
mensagem = mensagem.lower()
mensagem_criptografada = ''
for letra in mensagem:
    posição = alfabeto.find(letra)
    nova_posição = (posição - cifra)%26
    mensagem_criptografada += alfabeto[nova_posição]

print(mensagem_criptografada)
input()
