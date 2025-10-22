positivos_count = 0
positivos_soma = 0.0
for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos_count += 1
        positivos_soma += valor

print(f"{positivos_count} valores positivos")
if positivos_count > 0:
    media = positivos_soma / positivos_count
    print(f"{media:.1f}")