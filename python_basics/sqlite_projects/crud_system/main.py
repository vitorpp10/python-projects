from database import (
    criar_tabela,
    adicionar_funcionario,
    listar_funcionarios,
    atualizar_funcionario,
    excluir_funcionario
)

def menu():
    print("\n=== Sistema de Funcionários ===")
    print("1. Adicionar funcionário")
    print("2. Listar funcionários")
    print("3. Atualizar funcionário")
    print("4. Excluir funcionário")
    print("5. Sair")
    return input("Escolha uma opção: ")
    
def main():
    criar_tabela()  
    while True:
        opcao = menu()
        if opcao == '1':
            nome = input("Nome do funcionário: ").strip()
            if nome:
                adicionar_funcionario(nome)
                print("Funcionário adicionado!")
            else:
                print("Nome inválido.")
        elif opcao == '2':
            funcionarios = listar_funcionarios()
            print("--- Funcionários Cadastrados ---")
            for func in funcionarios:
                print(f"ID: {func[0]} | Nome: {func[1]}")
        elif opcao == '3':
            id = input("ID do funcionário a atualizar: ").strip()
            novo_nome = input("Novo nome: ").strip()
            if id.isdigit() and novo_nome:
                atualizar_funcionario(id, novo_nome)
                print("Funcionário atualizado!")
            else:
                print("Dados inválidos.")
        elif opcao == '4':
            id = input("ID do funcionário a excluir: ").strip()
            if id.isdigit():
                excluir_funcionario(id)
                print("Funcionário excluído!")
            else:
                print("ID inválido.")
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
