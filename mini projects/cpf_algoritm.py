import time
import sys
import os

def print_lento(texto, delay=0.05):
    texto_str = str(texto)
    for char in texto_str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


print_lento('CPF: ')
cpf = input()
clear_cpf = cpf.replace(".", "").replace("-", "")
print_lento(f'Seu cpf sem "." e "-": {clear_cpf}')
print()


print_lento('Colete a soma dos 9 primeiros dígitos do CPF \
multiplicando cada um dos valores por uma contagem regressiva começando de 10.             ')
print()


os.system('cls')


multiplication = (int(clear_cpf[0]) * 10) + (int(clear_cpf[1]) * 9) + \
(int(clear_cpf[2]) * 8) + (int(clear_cpf[3]) * 7) + (int(clear_cpf[4]) * 6) + \
(int(clear_cpf[5]) * 5)+ (int(clear_cpf[6]) * 4) + (int(clear_cpf[7]) * 3) \
+ (int(clear_cpf[8]) * 2)


print_lento('Resultado da multiplicação regressiva e soma = ')
print_lento(multiplication)
print()


os.system('cls')


print_lento('Multiplicar o resultado anterior por 10. ')
print()
multiplication2 = multiplication * 10


print_lento('Resultado da multiplicação anterior = ')
print_lento(multiplication2)
print()


os.system('cls')


print('Obter o resto da divisão da conta anterior por 11. ')
mod = multiplication2 % 11


print_lento('Resultado da divisão = ')
print_lento(mod)
print()


os.system('cls')


print_lento('Se o resultado anterior for maior que 9: \
resultado é 0 \
contrário disso: \
resultado é o valor da conta. ')
print()

print_lento("resultado = ")
print()

if mod > 9:

    x = 0

    print_lento(x)

else:

    print_lento(mod)