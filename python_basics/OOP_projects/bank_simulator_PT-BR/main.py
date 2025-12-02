from bank import Banco

import os
import time

def p(text, delay=0.05, end_with_newline=True):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def clear():
    os.system('cls' if os.name == 'nt' else clear)


def p_delay(text, delay=1.5):
    print(text)
    time.sleep(delay)


def input_delay(text, delay=0.05):
    p(text, delay=delay, end_with_newline=False)
    
    user_input = input()
    return user_input.strip() 



def main():
    clear()

    meu_banco = Banco('Banco Digital Dev')
    print('-' * 30)

    p('\nBem-vindo! Vamos criar sua conta para começar.', delay=0.03)

    while True:
        nome_titular = input_delay('Digite seu nome completo: ')
        if nome_titular:
            break
        p_delay('Nome não pode ficar vazio', delay=3)

    saldo_inicial = 0.0

    while True:
        try:
            saldo_str = input_delay('Digite seu depósito inicial (ex: 100.50): ')
            saldo_inicial= float(saldo_str)
            if saldo_inicial < 0:
                p_delay('Depósito inicial não pode ser negativo', delay=3)
            else:
                break
        except ValueError:
            p_delay('Valor inválido. Use ponto para decimais (ex: 50.00). ', delay=2)
    
    clear()
    
    conta_logada = meu_banco.abrir_conta(nome_titular, saldo_inicial)
    p_delay('Conta criada, acessando seu menu... ', delay=5)

    while True:
        clear()
        print(f"--- Menu Principal | {meu_banco.nome} ---")
        p(f"Olá, {conta_logada.titular}!")
        print("\nO que deseja fazer?")
        print("  1. Depositar")
        print("  2. Sacar")
        print("  3. Ver Saldo")
        print("  4. Sair")
    
        escolha = input_delay('Digite sua opção (1-4) ')
    
        if escolha == '1':
            try:
                valor_str = input_delay("Digite o valor para depósito: ")
                valor = float(valor_str)
                clear()
                p_delay("Processando depósito...", delay=5)
                conta_logada.depositar(valor)
            except ValueError:
                p_delay("Valor inválido. Tente novamente.", delay=2)

        elif escolha == '2':
            try:
                valor_str = input_delay("Digite o valor para saque: ")
                valor = float(valor_str)
                clear()
                p_delay("Verificando fundos e processando saque...", delay=5)
                conta_logada.sacar(valor)
            except ValueError:
                p_delay("Valor inválido. Tente novamente.", delay=2)
            
        elif escolha == '3':
            clear()
            p_delay("Consultando seu saldo...", delay=5)
            conta_logada.ver_saldo()
            
        elif escolha == '4':
            clear()
            p(f"Obrigado por usar o {meu_banco.nome}, {conta_logada.titular}!")
            p("Saindo...", delay=1)
            time.sleep(1)
            break
            
        else:
            p_delay("Opção inválida. Tente novamente.", delay=2)
        
        print("\nPressione ENTER para voltar ao menu...")
        input()

if __name__ == "__main__":
    main()