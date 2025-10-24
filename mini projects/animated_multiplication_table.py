import time
import os

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_multiplication(multipler):
    def multiplicatior(number):
        return number * multipler
    return multiplicatior

print_slow('Seu nome? ')
nome = str(input())
print()

print_slow(f'MULTIPLICAÇÕES DA {nome}')
print()
os.system('cls')

print_slow(f'{nome}, qual número deve ser multiplicado? ')
multiplier = int(input())
print()
print_slow('Ele deve ser multiplicado quantas vezes? ')
limit = int(input())
os.system('cls')

multi = create_multiplication(multiplier)

for i in range(1, limit + 1):
    number = multi(i)
    print_slow(f'{multiplier} x {i} = {number}!')
