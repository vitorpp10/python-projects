'''
def pegar(a, b, c): [def = definir] [pegar(a, b, c) nome da variavel para rodar oque esta em baixo e e seus parametros]
    print('a') [vai rodar se eu execuatar o pegar(1, 2, 3)]
    print('b') [vai rodar se eu execuatar o pegar(1, 2, 3)]
    print('c') [vai rodar se eu execuatar o pegar(1, 2, 3)]

pegar(1, 2, 3) [vai aparecer com os tres prints de cima]

programa para saber se z aparece ou nao

def soma(x, y, z=None): z é um valor vazio
    if z is not None: se z não for vazio, ou seja, a pessoa colocar o (0) la embaixo, ai ele executa o print
        print('tem z') é executado se a pessoa colocar um valor na hora de pedir ele
    else:
        print('nao tem z') senão não tem z, se não colocar o valor la embaixo

soma(1, 2) nao tem z
soma(1, 2, 0) tem z

se eu colocar:
soma(y=2, x=1) se eu usar "x=2" ou "y=1" ele pode ficar fora de ordem porque estaoa afirmando que y vai ser um no primerio argumento, entao ele redireciona para o segundo onde  eseu local
soma(1, 2) se eu nao usar "variavel=" tem que ser em ordem, porque la encima defini que x é o primeiro e y o segundo

escopo -> parte de dentro da def:
def x():
    x = 1 -> ta dentro de def, ou seja, dentro da função
x()

global - faz o escopo interno virar o externo, porque globalizou
x = 1
def x():
    global x -> pronto x vai ser o "1" inves do "2"
    x = 2
x()

call stack = onde salva cada função na hora do debug voltar ou mudar de escopo

return = retorna algo e deixa criar variaveis

def x():
    return x + y

sum1 = x(1, 2) retorna que sum1 e literal 3, ou seja, 2 + 1
sum2 = x(3, 4) retorna que sum2 e literal 7, ou seja, 3 + 4
sum_final = sum1 + sum2 -> soma final = 3 + 7 = 10
return tem que ser sempre o ultimo na função def, se for primeiro ele apaga o valor de baixo, que nem break do while

*args = juntar todos valores,
se seu def tiver muitos parametros voce pode usar *args que vai definir todos,

def x(*args):

x(1, 2, 3) -> nao vai dar erro, porque e como se esses 3 (1, 2, 3) tivesse no "*args"

OBS: serve como objetivo principal, passar argumentos nao nomeados, se voce analisar no exemplo do def, nao tem argumento dentro do seu escopo, ou seja,
eu defini o argumento dele no escopo do "x()" la embaixo, não no parametro do def, entao serve para argumentos nao nomeados no escopo do def,
e o "*args" fica no parametro para representar todos esses argumentos que nao foram nomeados la dentro para serem nomeados no escopo de "x()" la embaixo
''' 