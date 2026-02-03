import numpy as np

np.random.seed(42)
vendas = np.random.randint(10, 100, size=(5, 7))

print("Unidades vendidas (linhas=produtos, colunas=dias):\n", vendas)

total_por_produto = np.sum(vendas, axis=1)
media_por_produto = np.round(np.mean(vendas, axis=1), 1)

print("\nTotal de vendas por produto:", total_por_produto)
print("Média de vendas diárias por produto:", media_por_produto)

indice_mais_vendido = np.argmax(total_por_produto)
print(f"\nProduto mais vendido: Produto {indice_mais_vendido + 1} com {total_por_produto[indice_mais_vendido]} unidades")

total_geral = np.sum(vendas)
print(f"\nTotal geral de vendas na semana {total_geral}")

media_geral = np.round(np.mean(vendas), 1)
print(f"Média geral de vendas diárias: {media_geral} unidades")

destaques = media_por_produto > media_geral
print(destaques)

print("\nProdutos com média diária acima da média geral:")
for i, destaque in enumerate(destaques):
    if destaque:
        print(f"- Produto: {i + 1} (média: {media_por_produto[i]} unidades)")

