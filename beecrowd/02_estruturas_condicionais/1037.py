numero = float(input())

intervalo1 = 0 <= numero <= 25
intervalo2 = 25 < numero <= 50
intervalo3 = 50 < numero <= 75
intervalo4 = 75 < numero <= 100

texto_intervalo1 = '[0,25]'
texto_intervalo2 = '(25,50]'
texto_intervalo3 = '(50,75]'
texto_intervalo4 = '(75,100]'


if intervalo1:
    print(f'Intervalo {texto_intervalo1}')
elif intervalo2:
    print(f'Intervalo {texto_intervalo2}')
elif intervalo3:
    print(f'Intervalo {texto_intervalo3}')
elif intervalo4:
    print(f'Intervalo {texto_intervalo4}')
else:
    print('Fora de intervalo')