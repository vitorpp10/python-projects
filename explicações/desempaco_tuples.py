'''
desempacotamento

nome1, *resto = ['maria', 'helena', 'luiza']
nome1 virara 'maria',
"*" para dizer para o python pegar o resto da lista que colocar em um valor so, inves de colocar nome por nome, ficaria muito grande

para desempacotar:
lista = ['eu', 'ue'] lista com oque quero
nome1, nome2 = lista dando valor a cada coisa da lista

print(lista) mostrar na tela outpout

se for uma lista grande e quiser apenas alguns: 
lista = ['eu', 'ue', 'eu2', 'ue2', 'eu3', 'ue3', 'eu4', 'ue4'] lista com oque quero
nome1, nome5, nome8, *resto = lista escolhendo os valores que quero separado e o "*resto" para pegar tudo que nao quero de uma vez, assim nao preciso escrever nome por nome

print(lista) mostrar na tela outpout

"_" ignora mais facil:

_, nome, *_ = ['wu', 'yu', 'ikl', 'jk'] vai pegar o 'yu' como valor dois, e vai ignorar todo o resto
print(nome) mostrar na tela outpout

OBS: sempre de valor a cada variavel senao vai dar error, por isso do "*_"

tuplas:

tuplas sao listas imutaveis, ou seja, nao pode ser mexida que na lista normal acima
como fazer uma lista tuple?
nomes = ['a', 'b', 'c']
tuple(nomes)

ou 

nomes = 'a', 'b', 'c' -> so fazer sem "[]"

ou

nomes = ('a', 'b', 'c') so fazer com "()"

"enumerate" mesmo papel do range, porem melhor e mais pratico

"start=" começar de certo ponto
'''