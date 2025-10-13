### Gerar o Dataset Simulado — `new_dataset.py`

Cria o arquivo `dataset_vendas.csv` com mais 150 registros de vendas simuladas entre 01/01/2023 e 31/12/2023.
Os dados incluem as colunas:
`ID`, `Data`, `Produto`, `Categoria`, `Quantidade` e `Preço_unitario`.
O script também insere valores faltantes, duplicatas e erros intencionais para simular um cenário real de dados. Para que possa ser limpo depois

---

### Limpar o Dataset — `data_cleaner.py`

Lê o dataset original e realiza as seguintes etapas de limpeza:

- Preenche valores nulos (`Produto`, `Categoria`, `Quantidade`, `Preço_unitario`);
- Converte tipos de dados (`Data`, `Quantidade`);
- Remove registros inválidos e duplicados (baseado no `ID`);
- Gera um arquivo limpo: `data_clean.csv`.

---

### Operações e Análises — `operations.py`

Usa o dataset limpo para

- Calcular o total de vendas;
- Agrupar as vendas por produto e somar os valores;
- Identificar o produto com maior total de vendas;
- Exibir quantas vezes esse produto foi vendido.

### Visualização Gráfica — `analytics.py`

Analisa os dados e gera o gráfico `vendas_mensais_2023.png`, mostrando a tendência de vendas ao longo de 2023.
O script calcula o total de vendas por mês e utiliza o `matplotlib` para criar a visualização
