!pip install streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="OPA", page_icon="🛒", layout="wide")

# Título principal
st.title("OPA — Online Purchase Analysis")

# -----------------------------
# Carregar dados
# -----------------------------
@st.cache_data
def load_data():
    # Ajuste o caminho conforme onde o arquivo está
    df = pd.read_csv("/content/Profissão Cientista de Dados M29 - online_shoppers_intention.csv")
    return df

df = load_data()

st.subheader("Visualização inicial dos dados")
st.dataframe(df.head())

# -----------------------------
# Filtros interativos
# -----------------------------
st.sidebar.header("Filtros")

# Exemplo de filtro por mês
meses = df["Month"].unique().tolist()
mes_selecionado = st.sidebar.selectbox("Selecione o mês", meses)

# Exemplo de filtro por tipo de visitante
tipos = df["VisitorType"].unique().tolist()
tipo_selecionado = st.sidebar.selectbox("Selecione o tipo de visitante", tipos)

# Aplicar filtros
df_filtrado = df[(df["Month"] == mes_selecionado) & (df["VisitorType"] == tipo_selecionado)]

st.subheader(f"Dados filtrados — Mês: {mes_selecionado}, Visitante: {tipo_selecionado}")
st.dataframe(df_filtrado)

# -----------------------------
# Gráfico interativo
# -----------------------------
st.subheader("Distribuição de Revenue (compra realizada)")

fig, ax = plt.subplots()
df_filtrado["Revenue"].value_counts().plot(kind="bar", ax=ax, color=["green", "red"])
ax.set_xlabel("Revenue (True = compra, False = não)")
ax.set_ylabel("Quantidade")
st.pyplot(fig)

# -----------------------------
# Estatísticas simples
# -----------------------------
st.subheader("Estatísticas descritivas")
st.write(df_filtrado.describe())