import pandas as pd
import matplotlib.pyplot as plt

# === 1. Ler o Excel ===
arquivo ="C:\\Users\\valter.mascarenhas\\Downloads\\despesas_categorias.xlsx"   # coloque o caminho do seu ficheiro aqui
df = pd.read_excel(arquivo)

# Garantir que a coluna Mês é texto
#df["Mês"] = df["Mês"].astype(str)

# === 2. Escolher o mês ===
#mes_escolhido = "2026-01"   # pode trocar por input() se quiser
#df_mes = df[df["Mês"] == mes_escolhido]

# === 3. Resumo por categoria ===
resumo_categoria = df.groupby("Categoria")["Valor (€)"].sum().sort_values(ascending=False)

# === 4. Gráfico de Barras – por Categoria ===
plt.figure()
plt.bar(resumo_categoria.index, resumo_categoria.values)
plt.title(f"Gastos por Categoria")
plt.ylabel("Valor (€)")
plt.xlabel("Categoria")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 5. Evolução mensal (linha) ===
evolucao = df.groupby["Valor (€)"].sum().sort_index()

plt.figure()
plt.plot(evolucao.index, evolucao.values, marker='o')
plt.title("Evolução das Despesas Mensais")
plt.ylabel("Valor (€)")
plt.xlabel("Mês")
#plt.grid(True)
plt.tight_layout()
plt.show()
# === 6. Gráfico de Pizza – Distribuição das Despesas no Mês ===
plt.figure()
plt.pie(resumo_categoria.values, labels=resumo_categoria.index, autopct="%1.1f%%", startangle=90)
plt.title(f"Distribuição das Despesas")
plt.axis("equal")
plt.show()
# === Fim ===
