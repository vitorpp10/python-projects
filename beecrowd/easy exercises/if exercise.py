x = input('digite valor de x: ')
y = input('digite o valor de y: ')

if x > y:
    print(f'{x} é maior que {y}', 
          ', x é maior que y')
elif x < y:
    print(f'{x} é menor que {y}', 
          ', x é menor que y')
elif x == y:
    print(f'{x} é igual a {y}', 
          ', x é igual a y')