A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

tria = A * C / 2
circ = 3.14159 * C * C
trape = (A + B) * C / 2
square = B * B
rc = A * B

print(f'TRIANGULO: {tria:.3f}')
print(f'CIRCULO: {circ:.3f}')
print(f'TRAPEZIO: {trape:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {rc:.3f}')