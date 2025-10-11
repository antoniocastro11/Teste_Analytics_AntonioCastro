import pandas as pd 

df = pd.read_csv('data_clean.csv')

df['Total_vendas'] = df['Quantidade'] * df['Preço_unitario']

vendas_por_produto = df.groupby('Produto')['Total_vendas'].sum().reset_index().sort_values(by='Total_vendas', ascending=False)

produto_mais_vendido = vendas_por_produto.iloc[0]
quantidade_vendas = df[df['Produto'] == produto_mais_vendido['Produto']].shape[0]


print("Produto com maior venda:")
print(f"{produto_mais_vendido['Produto']}")
print(f"Quantidade de vendas realizadas: {quantidade_vendas}\n")


print("Total de vendas por produto:")
print(vendas_por_produto.to_string(index=False))