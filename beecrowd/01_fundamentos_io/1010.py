cd1, qtd1, preco1 = input().split()
cd1 = int(cd1)
qtd1 = int(qtd1)
preco1 = float(preco1)

cd2, qtd2, preco2 = input().split()
cd2 = int(cd2)
qtd2 = int(qtd2)
preco2 = float(preco2)


conta = (qtd1 * preco1) + (qtd2 * preco2)

print(f'VALOR A PAGAR: R$ {conta:.2f}')