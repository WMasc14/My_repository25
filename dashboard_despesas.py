import streamlit as st
import pandas as pd

st.set_page_config(page_title="Despesas Mensais", layout="centered")

# Seus dados
data = {
    "Categoria": [
        "Netflix", "HBO", "Apple TV", "DAZN", "Apple Cloud", "Crédito CGD",
        "Renda Casa", "Propina Curso", "Spotify", "Internet Telemóvel",
        "Seguro de Saúde", "Passe Navegante", "Ginásio", "Passe Verde Rodoviário",
        "Alimentação", "Seguro do Carro", "Combustível", "IUC", "Outros"
    ],
    "Valor (€)": [
        6.00, 0, 0, 17.00, 1.00, 245.00,
        400.00, 167.00, 0, 10.00,
        10.90, 40.00, 0, 0,
        250.00, 0, 0, 0, 135.00
    ]
}

df = pd.DataFrame(data)

# Total
total = df["Valor (€)"].sum()

st.title("📊 Dashboard de Despesas Mensais")

st.metric("💶 Total de Despesas", f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

st.subheader("📋 Tabela de Gastos")
st.dataframe(df, use_container_width=True)

st.subheader("📊 Gráfico de Barras")
st.bar_chart(df.set_index("Categoria"))

st.subheader("🥧 Gráfico de Pizza")
st.write("Distribuição percentual por categoria:")
st.dataframe(
    (df.assign(Percentual=df["Valor (€)"] / total * 100))
    .sort_values("Valor (€)", ascending=False)
    .style.format({"Valor (€)": "{:.2f}", "Percentual": "{:.1f}%"})
)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.pie(df["Valor (€)"], labels=df["Categoria"], autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

st.markdown("---")
st.markdown("© 2026 Dashboard de Despesas")
