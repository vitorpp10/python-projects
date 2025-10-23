nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

if ' ' in nome:
    print('seu nome tem espaços')
elif nome and idade:
    print('seu nome não tem espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a útima letra do seu nome é {nome[-1]}')
else:
    print('você deixou campos vazios, por favor preencha-os')