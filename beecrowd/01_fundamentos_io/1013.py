a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior1 = (a + b + abs(a - b)) / 2   
maior = (maior1 + c + abs(maior1 - c)) / 2
print(f'{int(maior)} eh o maior')