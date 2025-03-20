# Análise de Vendas de Jogos por Gênero

## Descrição do Projeto
Este projeto realiza uma análise de dados de vendas de jogos por gênero ao longo dos anos (2018-2021). O sistema utiliza Python com as bibliotecas Pandas, Matplotlib e Seaborn para criar visualizações e análises estatísticas dos dados de vendas.

## Funcionalidades

### 1. Visualização de Dados
- Exibe uma tabela completa com todos os dados de vendas
- Organiza os dados por ano e gênero
- Apresenta formatação clara e legível

### 2. Análises Estatísticas
O programa calcula e exibe as seguintes estatísticas por gênero:
- Média de vendas
- Valor mínimo de vendas
- Valor máximo de vendas
- Total de vendas
- Filtragem de vendas acima de 10 milhões

### 3. Visualizações Gráficas
O projeto gera dois gráficos principais:
1. **Gráfico de Linha**: 
   - Mostra a evolução das vendas por gênero ao longo dos anos
   - Inclui marcadores para cada ponto de dados
   - Possui legenda e grade para melhor visualização

2. **Gráfico de Barras**:
   - Apresenta a média de vendas por gênero
   - Inclui valores numéricos sobre cada barra
   - Utiliza formatação clara e legível

## Requisitos
Para executar o projeto, você precisa ter instalado:
```
pandas==2.1.0
matplotlib==3.7.2
seaborn==0.12.2
```

## Como Executar
1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o script:
```bash
python analise_jogos.py
```

## Estrutura dos Dados
O projeto trabalha com três categorias principais de jogos:
- Ação
- RPG
- Esporte

Os dados incluem:
- Anos: 2018 a 2021
- Vendas em milhões de unidades
- Análise por gênero de jogo

## Saída do Programa
Ao executar o script, você verá:
1. Tabela completa com todos os dados de vendas
2. Estatísticas detalhadas por gênero
3. Lista de vendas superiores a 10 milhões
4. Dois gráficos interativos:
   - Evolução temporal das vendas
   - Média de vendas por gênero

## Personalização
O código está estruturado de forma modular e pode ser facilmente modificado para:
- Adicionar novos gêneros de jogos
- Incluir mais anos de dados
- Criar análises estatísticas adicionais
- Modificar o estilo dos gráficos

## Observações
- Os dados utilizados são fictícios e servem apenas como exemplo
- As visualizações são otimizadas para legibilidade
- O código inclui comentários explicativos em cada seção 