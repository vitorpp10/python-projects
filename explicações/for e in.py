'''
"for" para cada
"in" entre

exemplo:

for x in x:
    print(x)

usar com indices ou iteraveis

"mostre maria, helena, e luiza na tela somente com indice"

lista = ['maria', 'helena', 'luiza'] lista para os nomes
indices = range(len(lista)) vai pegar o tamanho da lista e transformar a quantidade em numeros tudo na variavel "indices"

for indice in indices: para cada "indice" ou seja cada valor em "indices" que é a variavel, faça:
    print(lista[indice]) vai mostrar uma por uma em indices

EXTRAS:

".append()" adiciona um valor a lista sem te quer mudar, e ai o range ja dectecta isso e da valor a ele
"range" transforma cada valor em letra para representacao em numeros

'''