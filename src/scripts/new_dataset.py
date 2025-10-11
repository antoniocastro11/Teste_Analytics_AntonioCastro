import pandas as pd 
import numpy as np
import random
from datetime import datetime, timedelta

numRegistros = 150
inicio = datetime(2023, 1, 1)
fim = datetime(2023, 12, 31)

produtos =  {
    'Notebook': 'Eletrônicos',
    'Smartphone': 'Eletrônicos',
    'Fone de Ouvido': 'Eletrônicos',
    'Camiseta': 'Vestuário',
    'Tênis': 'Vestuário',
    'Calça': 'Vestuário',
    'Mochila': 'Acessórios',
    'Relógio': 'Acessórios',
    'Óculos': 'Acessórios',
}

np.random.seed(42)

dados = []
for i in range(numRegistros):
    produto = random.choice(list(produtos.keys()))
    categoria = produtos[produto]
    data_venda = inicio +timedelta(days=random.randint(0, (fim - inicio).days))
    quantidade = random.choice([1, 2, 3, 4, 5, np.nan])
    preco = round(random.uniform(50, 5000), 2)

    dados.append([i + 1, data_venda.date(), produto, categoria, quantidade, preco])

    df = pd.DataFrame(dados, columns=['ID', 'Data', 'Produto', 'Categoria', 'Quantidade', 'Preço_unitario'])


duplicados = df.sample(frac=0.05, random_state=1)
df = pd.concat([df, duplicados], ignore_index=True)

for col in['Produto', 'Categoria', 'Preço_unitario']:
    indicesNulos = df.sample(frac=0.05, random_state=random.randint(1, 100)).index
    df.loc[indicesNulos, col] = np.nan

df.sample = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv('dataset_vendas.csv', index=False, encoding='utf-8')