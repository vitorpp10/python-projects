import random

digits9 = ''
for i in range(9):
     digits9 += str(random.randint(0, 9))
    
cont1 = 10
result1 = 0

for i in digits9:
     result1 += int(digits9) * cont1
     cont1 -= 1
digit1 = (result1 * 10) % 11
digit1 = digit1 if digit1 <= 9 else 0

digits10 = digits9 + str(digit1)

cont2 = 11
result2 = 0

for i in digits10:
     result2 += int(digits10) * cont2
     cont2 -= 1
digit2 = (result2 * 10) % 11
digit2 = digit2 if digit2 <= 9 else 0

cpf = f'{digits9}{digit1}{digit2}'


print(cpf)