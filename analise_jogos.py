import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo e o tema do pandas para melhor visualização
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

# Configurando o estilo do seaborn para gráficos mais bonitos
sns.set_style("whitegrid")
plt.style.use("seaborn")

# Criando dados fictícios de forma mais organizada
anos = [2018] * 3 + [2019] * 3 + [2020] * 3 + [2021] * 3
generos = ['Ação', 'RPG', 'Esporte'] * 4
vendas = [12.5, 8.3, 6.7, 15.2, 10.1, 7.5, 18.6, 13.4, 5.9, 20.1, 15.8, 8.2]

# Criando o DataFrame
df = pd.DataFrame({
    'Ano': anos,
    'Gênero': generos,
    'Vendas (Milhões)': vendas
})

# Organizando o DataFrame por Ano e Gênero
df = df.sort_values(['Ano', 'Gênero'])

# Exibindo o DataFrame completo de forma organizada
print("\n=== DADOS DE VENDAS DE JOGOS POR GÊNERO ===")
print("\nTabela completa de vendas:")
print(df)

# Estatísticas básicas de forma mais organizada
print("\n=== ESTATÍSTICAS POR GÊNERO ===")
estatisticas = df.groupby('Gênero')['Vendas (Milhões)'].agg([
    ('Média', 'mean'),
    ('Mínimo', 'min'),
    ('Máximo', 'max'),
    ('Total', 'sum')
]).round(2)

print("\nEstatísticas de vendas por gênero:")
print(estatisticas)

# Filtrando vendas acima de 10 milhões
print("\n=== VENDAS ACIMA DE 10 MILHÕES ===")
vendas_altas = df[df['Vendas (Milhões)'] > 10].sort_values('Vendas (Milhões)', ascending=False)
print(vendas_altas)

# Configurando a visualização dos gráficos
plt.figure(figsize=(15, 6))

# Gráfico de linha
plt.subplot(1, 2, 1)
for genero in df['Gênero'].unique():
    dados_genero = df[df['Gênero'] == genero]
    plt.plot(dados_genero['Ano'], dados_genero['Vendas (Milhões)'], 
             marker='o', linewidth=2, markersize=8, label=genero)

plt.title('Evolução das Vendas por Gênero', fontsize=12, pad=15)
plt.xlabel('Ano', fontsize=10)
plt.ylabel('Vendas (Milhões)', fontsize=10)
plt.legend(title='Gênero', title_fontsize=10)
plt.grid(True, alpha=0.3)

# Gráfico de barras
plt.subplot(1, 2, 2)
media_por_genero = df.groupby('Gênero')['Vendas (Milhões)'].mean()
bars = plt.bar(media_por_genero.index, media_por_genero.values)
plt.title('Média de Vendas por Gênero', fontsize=12, pad=15)
plt.xlabel('Gênero', fontsize=10)
plt.ylabel('Média de Vendas (Milhões)', fontsize=10)

# Adicionando valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom')

# Ajustando o layout
plt.tight_layout()

# Mostrando os gráficos
plt.show() 