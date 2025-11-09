import os
import time
import sys

def print_lento(texto, delay=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

minha_lista = []

print_lento('Olá bem-vindo(a) á sua lista digital, qual seu nome?')
nome = str(input())
print()
print_lento(f'Olá {nome} é um prazer ter você conosco, vamos começar. ')
print()
print_lento('Qual o tipo da sua lista (compras, mercado etc)? ')
tipo_lista = str(input())
print()
print_lento(f'{tipo_lista} é uma ótima escolha {nome}! ')
print()

while True:
    print_lento('Selecione uma opção: ')
    print_lento('[i]nserir, [a]pagar, [l]istar: ')
    print()
    option = input()
    print()

    if option == 'i':
        os.system('cls')
        print_lento(f'Oque quer adicionar na sua lista de {tipo_lista} {nome}? ')
        value = input()
        minha_lista.append(value)
        print()
        print_lento(f'"{value}" foi adicionado a sua lista de {tipo_lista}, {nome}!')
        print()

    elif option == 'a':
        os.system('cls')
        
        print_lento(f'Sua lista de {tipo_lista} atual:')
        for item in minha_lista:
            print_lento(f'- {item}')
        print()

        print_lento(f'Oque quer apagar da sua lista de {tipo_lista} {nome}? ')
        value1 = input()
        print()
        
        minha_lista.remove(value1)
        
        print_lento(f'"{value1}" foi apagado da sua lista de {tipo_lista}, {nome}!')
        print()

    elif option == 'l':
        os.system('cls')
        print_lento(f'Aqui está sua lista de {tipo_lista} até agora: ')
        print()
        
        if not minha_lista:
            print_lento("... sua lista está vazia.")
        else:
            for item in minha_lista:
                print_lento(f'- {item}') 
        print()

    else:
        print_lento(f'Insira uma opção válida {nome}. ')
        continue