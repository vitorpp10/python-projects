'''
split -> serve para separar uma frase que contem espaços em branco
exemplo:
frase = 'oi x6, estou chegando' frase a ser separada
lista_frases = frases.split() demos um nome a variavel frase e adicionamos a função ".split()" e oque vai separar
print(lista_frases) mostrar na tela outpout

porem se colocarmos coisas dentro do parentese de split ele separa so oque voce colocou dentro ou seja os espaços
exemplo:
frase = 'oi x6, estou chegando' frase a ser separada
lista_frases = frases.split(', ') vai separar a PARTIR da "," e parar NO " ", so isso
print(lista_frases) mostrar na tela outpout

strip -> cortas os espaços do meio e do fim
exemplo:
frase = ' oi x6, estou chegando ' frase a ser separada
lista = frase.split(',') corta a partir da virgula
print(frase.strip) mostrar na tela outpout sem espaço sobrando entre os cortes

obs: rstrip -> corta somente o espaço da diretia
lstrip -> corta somente o espaço da esquerda

join -> cria a partir de uma str coloca oque quiser nessa str e depois o .join vai separar a partir do que voce digitou
exemplo:
frase = 'ola mundo' frase a ser separada
frases_join = 'separa'.join(frase) vai separar ela
'''