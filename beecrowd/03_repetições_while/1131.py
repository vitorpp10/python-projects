total_grenal = 0
inter_cont = 0
gremio_cont = 0
empates = 0

while True:
    inter, gremio = map(int, input().split())
    
    total_grenal = total_grenal + 1

    if inter > gremio:
        inter_cont = inter_cont + 1
    elif gremio > inter:
        gremio_cont = gremio_cont + 1
    else:
        empates = empates + 1

    print('Novo grenal (1-sim 2-nao)')
    value = int(input())
    
    if value == 2:
      break


print(f'{total_grenal} grenais')
print(f'Inter:{inter_cont}')
print(f'Gremio:{gremio_cont}')
print(f'Empates:{empates}')

if inter_cont > gremio_cont:
    print('Inter venceu mais')
elif gremio_cont > inter_cont:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')