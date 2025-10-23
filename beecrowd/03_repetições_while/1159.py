while True:
    x = int(input())
    if x == 0:
        break

    
    if x % 2 == 0:
        sum = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
        print(sum)
    else:
        x = x + 1
        sum = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
        print(sum) 