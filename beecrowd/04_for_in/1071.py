x = int(input())
y = int(input())

soma_impares = 0

if x < y:
    menor = x
    maior = y
else:
    menor = y
    maior = x

for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma_impares += i

print(soma_impares)