from abc import ABC, abstractmethod
import time
import os


def p(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def p_input(prompt, delay=0.08):
    p(prompt, delay)

    return input()

class Cores:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    RESET = '\033[0m'

class Produto(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def calcular_imposto(self):
        pass

class ProdutoEletronico(Produto):
    def calcular_imposto(self):
        return self.preco * 0.15

class ProdutoAlimenticio(Produto):
    def calcular_imposto(self):
        return self.preco * 0.05

from abc import ABC, abstractmethod 

def criar_produto():
    print('--- Cadastro de Novo Produto --- ')
    print()
    nome = p_input('Digite o nome do produto: ', delay=0.04)
    print()

    
    while True:
        try:
            preco_str = p_input('Digite o preço (R$): ', delay=0.04)
            clear()
            preco = float(preco_str)
            print() 

            if preco < 0:
                msg = Cores.AMARELO + 'Preço inválido. Digite um número positivo. ' + Cores.RESET
                p(msg)
                continue 
            else:
                break 
                
        except ValueError:
            msg = Cores.AMARELO + 'Entrada inválida. Digite apenas números para o preço. ' + Cores.RESET
            p(msg)
            p(' ', delay=0.04)
            clear()
            continue 
    
    clear()

    while True:
        p('Escolha o tipo:', delay=0.04)
        print('1 - Eletrônico (15% Imposto)')
        print('2 - Alimentício (5% Imposto)')
        print()

        tipo = p_input('Opção (1 ou 2): ', delay=0.04)
        print()
        clear()

        if tipo == '1':
            return ProdutoEletronico(nome, preco) 
            
        elif tipo == '2':
            return ProdutoAlimenticio(nome, preco) 
        
        else:
            msg = Cores.VERMELHO + 'Opção inválida. Tente 1 ou 2 ' + Cores.RESET
            p(msg)
            p(' ', delay=0.04)
            clear()
            continue 
            

def processar_imposto(produto: Produto):
    imposto = produto.calcular_imposto()
    print('Resultado do Processamento... ')
    p(' ', delay=2)
    clear()
    
    p(f'Produto: -> {produto.nome}, (R${produto.preco:.2f})', delay=0.07)
    p(f'Tipo: -> {produto.__class__.__name__}', delay=0.07)
    p(f'Imposto Aplicado: -> R${imposto:.2f}', delay=0.07)
    p(f'Preço Total (com imposto): -> R${produto.preco + imposto:.2f}', delay=0.07)
    print('----------------------------------')
    enter = p_input('Digite ENTER para continuar ', delay=0.04)
    if '' in enter:
        clear()

def main():
    list_ = []

    while True:
        p("=== Menu Principal ===", delay=0.02)
        print()
        print("1. Cadastrar Produto")
        print("2. Processar Todos os Impostos")
        print("3. Sair")
        print()

        escolha = p_input('Selecione uma opção: ', delay=0.02)
        clear()

        if escolha == '1':
                novo_produto = criar_produto()
                list_.append(novo_produto)
                print('Cadastrando Produto')
                p('... ', delay=2)
                print()
                clear()
                p(f"Produto '{novo_produto.nome}' cadastrado com sucesso!", delay=0.04)
                enter = p_input('Digite ENTER para continuar ', delay=0.02)
                if '' in enter:
                    clear()
                    continue
        
        elif escolha == '2':
            if not list_:
                msg = Cores.VERMELHO + 'Nenhum produto cadastrado para processar. ' + Cores.RESET
                p(msg)
                p(' ', delay=0.03)
                clear()
                continue
                

            print("\n==================================")
            print("INICIANDO PROCESSAMENTO DE IMPOSTOS")
            print("==================================")
            p('...', delay=2)
            print()

            for produto in list_:
                processar_imposto(produto)
        
        elif escolha == '3':
            print("Programa encerrado. Até mais!")
            print()
            break
    
        else:
            msg = Cores.VERMELHO + 'Opção inválida. Tente 1, 2 ou 3 ' + Cores.RESET
            p(msg)
            p(' ', delay=0.04)
            clear()

if __name__ == "__main__":
    main()
