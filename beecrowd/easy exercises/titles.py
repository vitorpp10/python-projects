'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.




Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.




Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
'''

#1
num = input('digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'número {num} é par')
    else:
        print(f'número {num} é impar')
else:
    print('não é um número inteiro') 


'''
.isdigit vai verificar se e int ou float
entao declara que o primeiro e int com num = int(num)
se for int ele vai fazer a verificação de par ou impar
o ultimo else e para caso o usuario digitar algo que seja float ou nao numero
'''

#2
hr = input("que horas é agora? ")

if hr.isdigit():
    hr = int(hr)
if hr >= 0 and hr <= 11:
    print('Bom dia')
elif hr >= 12 and hr <= 17:
    print('Boa tarde')
elif hr >= 18 and hr <= 23:
    print('Boa noite')
else:
    print('horas inválidas')


#3
nome = input('digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Nome curto. ', f'{nome} tem ', len(nome), ' caracteres. ')
elif tamanho >= 5 and tamanho <= 6:
    print('Nome normal, ', f'{nome} tem ', len(nome), ' caracteres. ')
else:
    print('Seu nome é muito grande, ', f'{nome} tem ', len(nome), ' caracteres. ')


