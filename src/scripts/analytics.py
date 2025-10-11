import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('data_clean.csv')

df["Data"] = pd.to_datetime(df["Data"], errors='coerce')

df['Total_vendas'] = df['Quantidade'] * df['Preço_unitario']

df['AnoMes'] = df['Data'].dt.to_period('M')

vendas_mensais = df.groupby('AnoMes')['Total_vendas'].sum().reset_index()

vendas_mensais['AnoMes'] = vendas_mensais['AnoMes'].dt.to_timestamp()  

plt.figure(figsize=(10, 5))
plt.plot(vendas_mensais['AnoMes'], vendas_mensais['Total_vendas'], marker='o', linestyle='-', linewidth=2)
plt.title('Vendas Mensais ao Longo do Ano de 2023')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (R$)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('vendas_mensais_2023.png')
plt.show()  

mes_maior_venda = vendas_mensais.loc[vendas_mensais["Total_vendas"].idxmax()]
mes_menor_venda = vendas_mensais.loc[vendas_mensais["Total_vendas"].idxmin()]

print("Insights:")
print(f"mês com MAIOR volume de vendas foi {mes_maior_venda['AnoMes'].strftime('%B/%Y')} com R$ {mes_maior_venda['Total_vendas']:.2f}.")
print(f"mês com MENOR volume de vendas foi {mes_menor_venda['AnoMes'].strftime('%B/%Y')} com R$ {mes_menor_venda['Total_vendas']:.2f}.")

media_vendas = vendas_mensais["Total_vendas"].mean()
if mes_maior_venda["Total_vendas"] > 1.5 * media_vendas:
    print("Pico de vendas considerável em um mês específico, provavelmente relacionado a promoções de Natal ou Black Friday.")
if mes_menor_venda["Total_vendas"] < 0.7 * media_vendas:
    print("Período de baixa acentuada, possivelmente por menor demanda após grandes eventos de compra.")