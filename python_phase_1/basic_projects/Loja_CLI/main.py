import datetime
import os
import time

def p(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def i(prompt, delay=0.04):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    
    user_input = input()
    return user_input


def record_transaction(prod, custo, venda, lucro):
    data_hoje = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    line = f'{data_hoje} | {prod} | Custo: R$ {custo:.2f} | Venda: R$ {venda:.2f} | Lucro: R$ {lucro:.2f}\n'

    try:
        with open('historico_vendas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(line)
        p('--> Salvo no histórico com sucesso!', delay=0.02)
    except Exception as e:
        p(f'\033[31mERRO ao salvar: {e}\033[0m', delay=0.02)

def ver_historico():
    clear()
    print('--- HISTÓRICO DE VENDAS (ÚLTIMOS 10 REGISTROS) ---')
    p(' ', delay=0.08)
    print('-' * 70)
    try:
        with open('historico_vendas.txt', 'r', encoding='utf-8') as arquivo:
            todas_linhas = arquivo.readlines()
        
        if not todas_linhas:
            p('O histórico de vendas está vazio.', delay=0.04)
            return 
        
        ultimas_transações = todas_linhas[-10:]
        
        for linha in ultimas_transações:
            print(linha.strip())

    except FileNotFoundError:
        p("\033[33mAviso: O arquivo 'historico_vendas.txt' ainda não existe.\033[0m", delay=0.04)
    
    except Exception as e:
        p(f"\033[31mERRO ao ler o arquivo: {e}\033[0m", delay=0.04)
    
    print('-' * 70)
    p('Pressione ENTER para voltar ao menu ', delay=0.04)
    input()
        
def calcular_lucro():
    clear()
    print('--- CALCULADORA DA LOJA --- ')

    try:
        produto = i('Nome do produto: ', delay=0.03)
        custo = float(i('Preço do Custo (R$): '))
        venda = float(i('Preço da Venda (R$): '))

        lucro = venda - custo
        
        if venda > 0:
            margem = (lucro / venda) * 100
        else:
            margem = 0.0

        print('\nRELAÇÃO: ')
        p(f'Lucro Bruto: R$ {lucro:.2f}', delay=0.03)
        p(f'Margem : {margem:.1f}%', delay=0.03)
    
        print()
        p('Pressione ENTER para continuar... ', delay=0.02)
        input()
        
        clear()
        print(f"Produto: {produto} | Lucro: R$ {lucro:.2f}")
        print("-" * 30)

        salvar = i('Deseja salvar essa transação no histórico? (s/n): ', delay=0.03)
        if salvar.lower().strip() == 's':
            record_transaction(produto, custo, venda, lucro)
        else:
            p('Transação não salva.', delay=0.03)
            time.sleep(1)

    except ValueError:
        clear()
        p('\033[31mERRO: O custo e o preço de vendas devem ser números válidos.\033[0m', delay=0.03)
        p('Retornando ao menu principal...')
        time.sleep(2)
    except Exception as e:
        p(f'\033[31mErro inesperado: {e}\033[0m')
        time.sleep(2)

def main():
    clear()
    p('--- SISTEMA LOJA CLI --- ')
    time.sleep(1)
    
    while True:
        clear()
        print('--- MENU PRINCIPAL ---')
        print('1. Nova Transação')
        print('2. Ver Histórico')
        print('3. Sair')
        print('-' * 30)
        
        opcao = i('Escolha uma opção: ', delay=0.02)
        
        if opcao == '1':
            calcular_lucro()
        elif opcao == '2':
            ver_historico()
        elif opcao == '3':
            clear()
            p("Sistema finalizado. Até logo!", delay=0.03)
            break
        else:
            p("Opção inválida! Tente novamente.", delay=0.03)
            time.sleep(1)



if __name__ == '__main__':
    main()
