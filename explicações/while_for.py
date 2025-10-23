"""
while = enquanto
ou seja,
quando algo que eu pedir não for concluido, ele não para, que nem no visualg

break = parar
ou seja,
para o programa a qualquer custo,
quando algo que você pedir for concluido, ele para, se não colocar nada ele so vai parar sem resposta
OBS: o break tem que ter um if para dar a causa de parar tambem, como falei la encima, se não colocar ele so para sem falar nada

continue = continuar de acordo com oque você colocou
ou seja,
se colocou para adicionar mais um ate 6 e depois mandou um if x == 6 / continue,
ele vai cortar o 6 e vai continuar,
ele pula oque você descrever
exemplo:

x = 0

while (enquanto) x < 10:
    x += 1 (x = x + 1)
    print(x) (sempre deixe o print aq, acho que é o melhor, não tenho certeza ainda)
    if x == 5:
        continue (vai pular o 5)
    
    if x <= 9:
        break
    
    print('acabou') (print depois do break, porque ai ja esta fora do programa e vai executar de qualquer jeito)

while dentro de while (um funcionar a partir do outro)
exemplo

x = 1
y = 1

while x <= 10
    y =+ 1
    while x <= 10
    x =+ 1

    if x == 10:
        break
        print('acabou')

enquanto x menor igual 10
    y adiciona + 1
    enquanto x menor igual 10
    x adiciona + 1

ou seja,
o x so vai adicionar +1 se o y for adiciona, então o segundo while depende do primeiro ser "true" ou funcionar

ATT CONTINUE:
se a afirmação que voce der for verdadeira pro continue ser executado, ele ira ignorar o codigo depois que vem em seguida do mesmo,
ou seja,
att continue = bom para fazer programas em que a pessoa digita errado e é punida

"""

