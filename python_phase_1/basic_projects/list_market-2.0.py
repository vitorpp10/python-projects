import os
import time
import sys

def p(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def clear():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

def delayed_input(prompt, delay=0.03):
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(delay)
    return input()  

lista = []
r_lista = []

x = 'listar'
y = 'desfazer'
z = 'refazer'

p('(se quiser rever comandos de um enter)\n                                               ', delay=0.06)
clear()

p(f'Comandos disponiveis: {x}, {y}, {z}\n ', delay=0.03)

while True:
     
    printt = delayed_input('Digite um dos comandos ou algum item para sua lista: ', delay=0.03)
    print()
    clear()

    
    if printt == '':
        p(f'Comandos disponiveis: {x}, {y}, {z}\n ', delay=0.03)
        b = input('ENTER para continuar ')
        if b == '':
            clear()
            continue
    elif printt.lower() == x:
        for i in range(len(lista)):
            print(f'Lista atual: {lista[i]}', end='\n')
            print()
        clear()
    elif printt.lower() == y:  
        if lista:
            remover = lista.pop()
            r_lista.append(remover)
            for i in range(len(lista)):
                p(f'{lista[i]}\n')
            print()
        else:
            p('Nada para desfazer\n')
            b = input('ENTER para continuar ')
            if b == '':
                clear()
            print()
    elif printt.lower() == z:
        if r_lista:
            remover = r_lista.pop()
            lista.append(remover)
            for i in range(len(lista)):
                p(f'{lista[i]}\n')
            print()
        else:
            p('Nada para refazer\n')
            b = input('ENTER para continuar ')
            if b == '':
                clear()
            print()
    else:
        lista.append(printt)
        for i in range(len(lista)):
            p(f'{lista[i]}\n')
        r_lista.clear()
        print()
        a = delayed_input('Deseja continuar (y/n)? ')
        if a == 'y':
            clear()
            continue
        else:
            for i in range(len(lista)):
                p('Sua lista final: ', delay=0.02)
                p(f'{lista[i]}\n', delay=0.02)
            break