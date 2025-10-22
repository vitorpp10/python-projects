x, y = map(int, input().split())

if x == 1:
    total = 4 * y
    print(f'Total: R$ {total:.2f}')
elif x == 2:
    total = 4.50 * y
    print(f'Total: R$ {total:.2f}')
elif x == 3:
    total = 5 * y
    print(f'Total: R$ {total:.2f}')
elif x == 4:
    total = 2 * y
    print(f'Total: R$ {total:.2f}')
elif x == 5:
    total = 1.50 * y
    print(f'Total: R$ {total:.2f}')