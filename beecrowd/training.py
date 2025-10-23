'''
1015 beecrowd

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
distance_final = math.sqrt(distance)

print(f'{distance_final:.4f}')
'''

'''
1016 beecrowd

distance = int(input())

temp_min = distance * 2

print(f'{temp_min} minutos')
'''

'''
1017 beecrowd

temp_work = int(input())
velocity_media = int(input())

distance = temp_work * velocity_media
necessary_L = distance / 12

print(f'{necessary_L:.3f}')
'''

'''
1018 beecrowd

value = int(input())

quanty1 = value // 100
rest1 = value % 100

quanty2 = rest1 // 50
rest2 = rest1 % 50

quanty3 = rest2 // 20
rest3 = rest2 % 20

quanty4 = rest3 // 10
rest4 = rest3 % 10

quanty5 = rest4 // 5
rest5 = rest4 % 5

quanty6 = rest5 // 2
rest6 = rest5 % 2

quanty7 = rest6 // 1
rest7 = rest6 % 1

print(f'{value}')
print(f'{quanty1} nota(s) de R$ 100,00')
print(f'{quanty2} nota(s) de R$ 50,00')
print(f'{quanty3} nota(s) de R$ 20,00')
print(f'{quanty4} nota(s) de R$ 10,00')
print(f'{quanty5} nota(s) de R$ 5,00')
print(f'{quanty6} nota(s) de R$ 2,00')
print(f'{quanty7} nota(s) de R$ 1,00')
'''

'''
1019 beecrowd

value = int(input())

hours = value // 3600
rest_before_hours = value % 3600
minutes = rest_before_hours // 60
seconds = rest_before_hours % 60

print(f'{hours}:{minutes}:{seconds}')
'''

'''
1020 beecrowd

value = int(input())

year = value // 365
rest_of_year = value % 365
month = rest_of_year // 30
days = rest_of_year % 30

print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{days} dia(s)')
'''

'''
1021 beecrowd

value = float(input())
value_in_cents = int(value * 100)

# notas:

quanty1 = value_in_cents // 10000
rest1 = value_in_cents % 10000

quanty2 = rest1 // 5000
rest2 = rest1 % 5000

quanty3 = rest2 // 2000
rest3 = rest2 % 2000

quanty4 = rest3 // 1000
rest4 = rest3 % 1000

quanty5 = rest4 // 500
rest5 = rest4 % 500

quanty6 = rest5 // 200
rest6 = rest5 % 200

# moedas:

quanty7 = rest6 // 100
rest7 = rest6 % 100

quanty8 = rest7 // 50
rest8 = rest7 % 50

quanty9 = rest8 // 25
rest9 = rest8 % 25

quanty10 = rest9 // 10
rest10 = rest9 % 10

quanty11 = rest10 // 5
rest11 = rest10 % 5

quanty12 = rest11 // 1
rest12 = rest11 % 1

print('NOTAS:')
print(f'{quanty1:.0f} nota(s) de R$ 100.00')
print(f'{quanty2:.0f} nota(s) de R$ 50.00')
print(f'{quanty3:.0f} nota(s) de R$ 20.00')
print(f'{quanty4:.0f} nota(s) de R$ 10.00')
print(f'{quanty5:.0f} nota(s) de R$ 5.00')
print(f'{quanty6:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{quanty7:.0f} moeda(s) de R$ 1.00')
print(f'{quanty8:.0f} moeda(s) de R$ 0.50')
print(f'{quanty9:.0f} moeda(s) de R$ 0.25')
print(f'{quanty10:.0f} moeda(s) de R$ 0.10')
print(f'{quanty11:.0f} moeda(s) de R$ 0.05')
print(f'{quanty12:.0f} moeda(s) de R$ 0.01')
'''

'''
1040 beecrowd

n1, n2, n3, n4 = map(float, input().split())
wmedia = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
print(f'Media: {wmedia:.1f}')

if wmedia >= 7:
    print('Aluno aprovado.')
elif wmedia < 5:
    print('Aluno reprovado.') 
elif wmedia >= 5 and wmedia <= 6.9:
    print('Aluno em exame.')
    nota = float(input())
    print(f'Nota do exame: {nota:.1f}')
    media_final = (nota + wmedia) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
    elif media_final <= 4.9:
        print('Aluno reprovado.')
    
    print(f'Media final: {media_final:.1f}')
'''

'''
1041 beecrowd 

x, y = map(float, input().split())

if x == 0 and y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
'''

'''
1042 beecrowd

x, y, z = map(int, input().split())

if x > y > z:
    print(z)
    print(y)
    print(x)
elif x > z > y:
    print(y)
    print(z)
    print(x)
elif y > x > z:
    print(z)
    print(x)
    print(y)
elif y > z > x:
    print(x)
    print(z)
    print(y)
elif z > y > x:
    print(x)
    print(y)
    print(z)
elif z > x > y:
    print(y)
    print(x)
    print(z)

print()
print(x)
print(y)
print(z)
'''

'''
1043 beecrowd

A, B, C = map(float, input().split())

if (A + B > C) and (A + C > B) and (B + C > A) == True:
    per = A + B + C
    print(f'Perimetro = {per:.1f}')
else:
    area = ((A + B) * C) / 2
    print(f'Area = {area:.1f}')
'''

'''
1044 beecrowd
A, B = map(int, input().split())

mult = (A % B == 0) or (B % A == 0)

if mult:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
'''

'''
1045 beecrowd

v1, v2, v3 = map(float, input().split())

if v1 >= v2 and v1 >= v3:
    A = v1
    if v2 >= v3:
        B = v2
        C = v3
    else:
        B = v3
        C = v2
elif v2 >= v1 and v2 >= v3:
    A = v2
    if v1 >= v3:
        B = v1
        C = v3
    else:
        B = v3
        C = v1
else:
    A = v3
    if v1 >= v2:
        B = v1
        C = v2
    else:
        B = v2
        C = v1


if A >= B + C:
    print('NAO FORMA TRIANGULO')
else: 
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')

if A == B and B == C:
    print('TRIANGULO EQUILATERO')
elif A == B or B == C or A == C:
    print('TRIANGULO ISOSCELES')
'''

'''
1046 beecrowd

s, e = map(int, input().split())

if e > s:
    d1 = e - s
    print(f'O JOGO DUROU {d1} HORA(S)')
elif e <= s:
    d2 = (24 - s) + e
    print(f'O JOGO DUROU {d2} HORA(S)')

'''

'''
1047 beecrowd

h1, m1, h2, m2 = map(int, input().split())

im = (h1 * 60) + m1
fm = (h2 * 60) + m2

if fm > im:
    duration = fm - im
else:
    duration = (24 * 60 - im) + fm

h = duration // 60
m = duration % 60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
'''