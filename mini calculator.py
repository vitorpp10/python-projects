import math

# ===================================================================
# Bloco 1: Boas-Vindas (Executa apenas uma vez)
# ===================================================================
nome = input('Digite seu nome: ')
print(' ')
print(f'{nome}, bem-vindo(a) a sua calculadora em Python!')
print('Para selecionar uma operação, basta digitar o número correspondente.')
print('Bom uso!')
print('\n======================================================\n')


# ===================================================================
# Bloco 2: Loop Principal (Mantém a calculadora funcionando)
# ===================================================================
while True:
    print('====== MENU PRINCIPAL ======')
    print('1: Soma (+)')
    print('2: Subtração (-)')
    print('3: Multiplicação (*)')
    print('4: Divisão (/)')
    print('5: Mais opções...')
    print('9: Sair do Programa')
    print(' ')
    
    value = input("Digite o número da opção desejada: ")
    print(' ')

    # --- Condição de Saída ---
    if value == '9':
        print(f'Obrigado por usar a calculadora, {nome}. Até mais!')
        break # Encerra o loop while e finaliza o programa

    # --- Operações Básicas ---
    elif value == "1":
        print('-> SOMA')
        print('Digite os dois números a serem somados (separados por espaço):')
        s1, s2 = map(float, input().split())
        soma = s1 + s2
        print(' ')
        print(f'Resultado: {s1} + {s2} = {soma}')
    
    elif value == "2":
        print('-> SUBTRAÇÃO')
        print('Digite os dois números a serem subtraídos (separados por espaço):')
        sb1, sb2 = map(float, input().split()) # Alterado para float para consistência
        sub = sb1 - sb2
        print(' ')
        print(f'Resultado: {sb1} - {sb2} = {sub}')
    
    elif value == "3":
        print('-> MULTIPLICAÇÃO')
        print('Digite os dois números a serem multiplicados (separados por espaço):')
        m1, m2 = map(float, input().split()) # Alterado para float para consistência
        mult = m1 * m2
        print(' ')
        print(f'Resultado: {m1} * {m2} = {mult}')
    
    elif value == "4":
        print('-> DIVISÃO')
        print('Digite o dividendo e o divisor (separados por espaço):')
        d1, d2 = map(float, input().split())
        if d2 == 0:
            print('Erro: Divisão por zero não é permitida.')
        else:
            div = d1 / d2
            print(' ')
            print(f'Resultado: {d1} / {d2} = {div}')

    # --- Sub-menu de Mais Opções ---
    elif value == '5':
        print('--- Mais Opções ---') 
        print('6: Média de dois números')
        print('7: Raiz quadrada')
        print('8: Exponenciação (Potência)')
        print('0: Voltar ao menu principal')
        print(' ')
        
        value1 = input('Qual opção você deseja? ')
        print(' ')
        
        if value1 == "6":
            print('-> MÉDIA')
            print('Digite os dois números para calcular a média (separados por espaço):')
            me1, me2 = map(float, input().split())
            media = (me1 + me2) / 2
            print(' ')
            print(f'Resultado: A média de {me1} e {me2} é {media}')
        
        elif value1 == "7":
            print('-> RAIZ QUADRADA')
            print('Digite o número para extrair a raiz quadrada:')
            r1 = float(input())
            if r1 < 0:
                print('Erro: Não é possível calcular a raiz de um número negativo.')
            else:
                raiz_final = math.sqrt(r1)
                print(' ')
                print(f'Resultado: A raiz quadrada de {r1} é {raiz_final}')
        
        elif value1 == "8":
            print('-> EXPONENCIAÇÃO')
            print('Digite a base e o expoente (separados por espaço):')
            base, expoente = map(float, input().split())
            resultado_expo = base ** expoente
            print(' ')
            print(f'Resultado: {base} elevado a {expoente} é {resultado_expo}')
        
        elif value1 == '0':
            print('Voltando ao menu principal...')
            # 'continue' pula para a próxima iteração do loop, mostrando o menu novamente
            print('\n------------------------------------------------------\n')
            continue
        
        else:
            print("Opção inválida. Voltando ao menu principal.")

    # --- Tratamento de Opção Inválida no Menu Principal ---
    else:
        print("Opção inválida. Por favor, selecione um número do menu.")

    # Mensagem de separação antes do loop recomeçar
    print('\n------------------------------------------------------\n')