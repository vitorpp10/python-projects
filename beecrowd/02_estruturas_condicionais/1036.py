import math

A, B, C = map(float, input().split())

delta = B ** 2 - 4 * A * C
x = 0 
y = 0

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz_delta = math.sqrt(delta)

    x = (-B + raiz_delta) / (2 * A)
    y = (-B - raiz_delta) / (2 * A)

    print(f'R1 = {x:.5f}')
    print(f'R2 = {y:.5f}')