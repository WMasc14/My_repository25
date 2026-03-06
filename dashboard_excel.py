
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("📊 Dashboard Financeiro Mensal")

uploaded_file = st.file_uploader("📂 Carregue o Excel com coluna Mês", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Normalizar coluna Mês
    df["Mês"] = df["Mês"].astype(str)

    # Filtros
    meses = sorted(df["Mês"].unique())
    mes_selecionado = st.selectbox("📅 Selecionar Mês:", meses, index=len(meses)-1)

    df_mes = df[df["Mês"] == mes_selecionado]

    total_mes = df_mes["Valor (€)"].sum()

    st.metric("💶 Total do Mês", f"{total_mes:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Total por Categoria")
        resumo = df_mes.groupby("Categoria")["Valor (€)"].sum().sort_values(ascending=False)
        st.bar_chart(resumo)

    with col2:
        st.subheader("🥧 Percentual por Categoria")
        pct = (resumo / total_mes * 100).round(1)
        st.dataframe(pct.rename("Percentual (%)"))

    st.divider()

    st.subheader("📈 Comparação entre Meses")

    comparacao = df.groupby("Mês")["Valor (€)"].sum().sort_index()
    st.line_chart(comparacao)

    st.divider()

    st.subheader("🎯 Metas por Categoria")

    metas = {}
    for cat in df["Categoria"].unique():
        metas[cat] = st.number_input(f"Meta para {cat} (€)", min_value=0.0, value=0.0, step=10.0)

    st.subheader("🚨 Alertas do Mês Selecionado")
    for cat, meta in metas.items():
        gasto = df_mes[df_mes["Categoria"] == cat]["Valor (€)"].sum()
        if meta > 0 and gasto > meta:
            st.error(f"⚠️ {cat}: {gasto:.2f} € (Meta: {meta:.2f} €)")

else:
    st.info("👆 Faça upload do Excel para iniciar o dashboard.")
    