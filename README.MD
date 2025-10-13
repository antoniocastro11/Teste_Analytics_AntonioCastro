# Projeto de Análise de Vendas - Teste técnico Quod

## Antonio G. Castro

Este respositório simula um dataset "sujo", limpa, analisa e visualiza um conjunto de dados de vendas referentes ao ano de 2023.  
Ele foi desenvolvido em Python com o uso de bibliotecas de manipulação de dados e geração de gráficos. E consultas SQL.

---

## Estrutura do Repositório

`queries/consultas_sql.sql`: Consultas SQL para análise de vendas

`scripts/..:` cria dadaset, limpa dataset, faz operações e gera gráfico

---

## Bibliotecas

O projeto utiliza as seguintes bibliotecas:

- **pandas**: manipulação e limpeza de dados
- **numpy**: geração de números aleatórios e cálculos
- **matplotlib**: criação de gráficos e visualizações
- **datetime**: manipulação de datas
- **random** : simulação de dados aleatórios

### Instalação das dependências:

```bash
pip install pandas numpy matplotlib
```

---

## Execução dos Scripts

A sequência recomendada para executar o projeto é:

1. **Gerar o dataset simulado**: new_dataset.py

2. **Limpar o dataset**: data_cleaner.py

3. **Realizar operações analíticas**: operations.py

4. **Gerar análises gráficas** analytics.py

---

## Consultas SQL

As consultas SQL estão no arquivo: consultas_sql.sql

- Calcula o total de vendas por produto e categoria;
- Identifica produtos com menor volume de vendas em junho de 2023 (na instrução estava 2024, todavia, a instrução de simualação do dataset era até fim de 2023, logo, optei por deixar junho de 2023).
