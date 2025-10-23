n = int(input())
for _ in range(n):
    valor = int(input())
    
    if valor == 0:
        print("NULL")
    elif valor > 0:
        if valor % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    else: 
        if valor % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")