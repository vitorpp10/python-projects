A, B, C, D = map(int, input().split())

condicao1 = B > C
condicao2 = D > A
condicao3 = C + D > A + B
condicao4 = C > 0
condicao5 = D > 0
condicao6 = A % 2 == 0

if (condicao1) and (condicao2) and (condicao3) and (condicao4) and (condicao5) and (condicao6):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')