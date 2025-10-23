notas_validas_contadas = 0
soma_das_notas = 0

# 2. O loop roda enquanto não tivermos encontrado 2 notas válidas
while notas_validas_contadas < 2:
    
    # 3. Leia UMA nota
    nota = float(input())
    
    # 4. Verifique se é válida
    if 0 <= nota <= 10:
        # Se for, atualize nossas variáveis de controle
        soma_das_notas = soma_das_notas + nota  # Adiciona a nota à soma
        notas_validas_contadas = notas_validas_contadas + 1 # Incrementa o contador
    else:
        # Se não for, apenas avise e o loop continuará
        print('nota invalida')

# 5. O loop só acaba quando temos a soma de 2 notas válidas
media = soma_das_notas / 2

# 6. Imprima o resultado final
print(f'media = {media:.2f}')