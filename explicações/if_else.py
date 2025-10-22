"""
entrada = input("Quer 'entrar' ou 'sair'?")

if entrada == 'entrar':
    print("Você entrou no sistema")
elif entrada == 'sair':
    print("Você saiu do sistema")
else:
    print("Digite somente 'entrar' ou 'sair'")
"""

nome = input("Digite o nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))
salário = int(input("Digite o salário do usuário: "))

if idade > 17:
    print(f'{nome} tema mais de 18 anos')
else:
    print(f'{nome} tem menos de 18 anos')

if salário > 1499:
    print(f'{nome} ganha mais de 1500 reais')
else:
    print(f'{nome} ganha menos de 1500 reais')