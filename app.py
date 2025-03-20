import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando a página
st.set_page_config(page_title="Análise de Vendas de Jogos", layout="wide")

# Título
st.title("Análise de Vendas de Jogos por Gênero")

# Criando dados
dados = {
    'Ano': [2018] * 3 + [2019] * 3 + [2020] * 3 + [2021] * 3,
    'Gênero': ['Ação', 'RPG', 'Esporte'] * 4,
    'Vendas (Milhões)': [12.5, 8.3, 6.7, 15.2, 10.1, 7.5, 18.6, 13.4, 5.9, 20.1, 15.8, 8.2]
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Organizando o DataFrame
df = df.sort_values(['Ano', 'Gênero'])

# Mostrando os dados
st.header("Dados de Vendas")
st.dataframe(df)

# Estatísticas
st.header("Estatísticas por Gênero")
estatisticas = df.groupby('Gênero')['Vendas (Milhões)'].agg([
    ('Média', 'mean'),
    ('Mínimo', 'min'),
    ('Máximo', 'max'),
    ('Total', 'sum')
]).round(2)

st.dataframe(estatisticas)

# Gráficos
st.header("Visualizações")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolução das Vendas por Gênero")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    for genero in df['Gênero'].unique():
        dados_genero = df[df['Gênero'] == genero]
        ax1.plot(dados_genero['Ano'], dados_genero['Vendas (Milhões)'], 
                marker='o', linewidth=2, markersize=8, label=genero)
    
    ax1.set_title('Evolução das Vendas por Gênero')
    ax1.set_xlabel('Ano')
    ax1.set_ylabel('Vendas (Milhões)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    st.pyplot(fig1)

with col2:
    st.subheader("Média de Vendas por Gênero")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    media_por_genero = df.groupby('Gênero')['Vendas (Milhões)'].mean()
    bars = ax2.bar(media_por_genero.index, media_por_genero.values)
    
    ax2.set_title('Média de Vendas por Gênero')
    ax2.set_xlabel('Gênero')
    ax2.set_ylabel('Média de Vendas (Milhões)')
    
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom')
    
    st.pyplot(fig2)

# Adicionar filtros interativos
st.sidebar.header("Filtros")
anos_selecionados = st.sidebar.multiselect(
    "Selecione os Anos",
    options=df['Ano'].unique(),
    default=df['Ano'].unique()
)

generos_selecionados = st.sidebar.multiselect(
    "Selecione os Gêneros",
    options=df['Gênero'].unique(),
    default=df['Gênero'].unique()
)

# Dados filtrados
df_filtrado = df[
    (df['Ano'].isin(anos_selecionados)) &
    (df['Gênero'].isin(generos_selecionados))
]

st.header("Dados Filtrados")
st.dataframe(df_filtrado) 