import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Dados de exemplo (você pode trocar pelos seus)
data = {
    "Categoria": ["Aluguel", "Alimentação", "Transporte", "Lazer", "Internet", "Outros"],
    "Valor": [1200, 600, 300, 250, 120, 180]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="Dashboard de Despesas", layout="centered")

st.title("📊 Dashboard de Despesas Mensais")

st.subheader("Tabela de Gastos")
st.dataframe(df)

st.subheader("Gráfico de Pizza – Distribuição das Despesas")

fig, ax = plt.subplots()
ax.pie(df["Valor"], labels=df["Categoria"], autopct="%1.1f%%", startangle=90)
ax.axis("equal")

st.pyplot(fig)

st.subheader("Gráfico de Barras – Gastos por Categoria")

fig2, ax2 = plt.subplots()
ax2.bar(df["Categoria"], df["Valor"])
ax2.set_ylabel("Valor (R$)")
ax2.set_xlabel("Categoria")

st.pyplot(fig2)
