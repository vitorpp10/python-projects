nome = input()
salario_fixo = float(input())
salario_mes = float(input())

conta_final = (salario_mes * 0.15) + salario_fixo

print(f'TOTAL = R$ {conta_final:.2f}')