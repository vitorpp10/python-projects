
while True:
    
 
    soma_das_notas = 0
    notas_validas_contadas = 0
    
  
    while notas_validas_contadas < 2:
        nota = float(input())
        
        if 0 <= nota <= 10:
            soma_das_notas = soma_das_notas + nota
            notas_validas_contadas = notas_validas_contadas + 1
        else:
            print('nota invalida')
            
    
    media = soma_das_notas / 2
    print(f'media = {media:.2f}')



    
    print('novo calculo (1-sim 2-nao)')
    opcao = int(input())
    
   
    while opcao != 1 and opcao != 2:
        print('novo calculo (1-sim 2-nao)')
        opcao = int(input())
        
    if opcao == 2:
        break 