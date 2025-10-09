import pandas as pd
import numpy as np

df = pd.read_csv('dataset_vendas.csv')

df['Quantidade'].fillna(1, inplace=True)
df['Produto'].fillna('Produto Desconhecido', inplace=True)
df['Categoria'].fillna('Categoria Desconhecida', inplace=True)
df['Preço'].fillna(df['Preço'].median(), inplace=True)

df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors='coerce')

df = df[df['Quantidade'].notna()]
df = df[df['Quantidade'] > 0]
df = df[df['Preço'] > 0]
df = df[df['Preço'] < 100000]

df = df.drop_duplicates(subset="ID", keep="first")

df.reset_index(drop=True, inplace=True)
df.to_csv('data_clean.csv', index=False, encoding='utf-8')