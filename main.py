import streamlit as st
import pandas as pd


# =====================================
# CONFIGURAÇÃO
# =====================================

st.set_page_config(
    page_title="Impacto da IA",
    page_icon="🤖",
    layout="wide"
)


# =====================================
# TÍTULO DO APP
# =====================================

st.title("🤖 Impacto da Inteligência Artificial no Desempenho Acadêmico")

st.header("Projeto de Programação em Python")

st.markdown("""
Este aplicativo apresenta uma análise sobre como o uso da Inteligência Artificial
pode influenciar o desempenho acadêmico dos estudantes.
""")


# =====================================
# IMPORTANDO OS DADOS
# =====================================

@st.cache_data
def carregar_dados():

    df = pd.read_csv("ai_student_impact_dataset.csv")


    df = df.rename(columns={
        "Student_ID": "ID Estudante",
        "Major_Category": "Área do Curso",
        "Year_of_Study": "Ano de Estudo",
        "Pre_Semester_GPA": "Nota Antes do Semestre",
        "Weekly_GenAI_Hours": "Horas Semanais Usando IA",
        "Primary_Use_Case": "Principal Uso IA",
        "Traditional_Study_Hours": "Horas de Estudo Tradicional",
        "Post_Semester_GPA": "Nota Depois do Semestre",
        "Burnout_Risk_Level": "Risco de Burnout"
    })


    # cálculo usado no seu trabalho
    df["Variação da Nota"] = (
        df["Nota Depois do Semestre"]
        -
        df["Nota Antes do Semestre"]
    )


    return df



df = carregar_dados()



# =====================================
# SIDEBAR
# =====================================

st.sidebar.header("Filtros")


curso = st.sidebar.selectbox(
    "Selecione a área do curso",
    ["Todos"] + list(df["Área do Curso"].unique())
)


ano = st.sidebar.selectbox(
    "Selecione o ano de estudo",
    ["Todos"] + list(df["Ano de Estudo"].unique())
)



# aplicando filtros

df_filtrado = df.copy()


if curso != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["Área do Curso"] == curso
    ]


if ano != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["Ano de Estudo"] == ano
    ]



# =====================================
# INDICADORES
# =====================================

st.header("📊 Indicadores Gerais")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Número de estudantes",
        len(df_filtrado)
    )


with col2:

    st.metric(
        "Média da nota final",
        round(
            df_filtrado["Nota Depois do Semestre"].mean(),
            2
        )
    )


with col3:

    st.metric(
        "Horas médias de IA",
        round(
            df_filtrado["Horas Semanais Usando IA"].mean(),
            2
        )
    )



# =====================================
# TABELA
# =====================================

st.header("📋 Visualização dos dados")


st.write(
    "Primeiras linhas do conjunto de dados:"
)


st.dataframe(
    df_filtrado.head(10)
)

# =====================================
# VARIAÇÃO DA NOTA POR USO DE IA
# =====================================

st.header("📈 Variação média da nota por uso de IA")


# criando grupos

pouco_uso = df_filtrado[
    df_filtrado["Horas Semanais Usando IA"] <= 3
]


uso_medio = df_filtrado[
    (df_filtrado["Horas Semanais Usando IA"] > 3) &
    (df_filtrado["Horas Semanais Usando IA"] <= 8)
]


uso_alto = df_filtrado[
    df_filtrado["Horas Semanais Usando IA"] > 8
]


# calculando médias

media_pouco = pouco_uso["Variação da Nota"].mean()

media_medio = uso_medio["Variação da Nota"].mean()

media_alto = uso_alto["Variação da Nota"].mean()



# criando tabela para gráfico

grafico_ia = pd.DataFrame({

    "Nível de uso da IA": [
        "Pouco uso",
        "Uso médio",
        "Uso alto"
    ],

    "Variação média da nota": [
        media_pouco,
        media_medio,
        media_alto
    ]

})


st.write(grafico_ia)



# gráfico

st.bar_chart(
    grafico_ia,
    x="Nível de uso da IA",
    y="Variação média da nota"
)
# =====================================
# VARIAÇÃO DA NOTA POR ESTUDO TRADICIONAL
# =====================================

st.header("📚 Variação média da nota por tempo de estudo tradicional")


# criando grupos

pouco_estudo = df_filtrado[
    df_filtrado["Horas de Estudo Tradicional"] <= 3
]


estudo_medio = df_filtrado[
    (df_filtrado["Horas de Estudo Tradicional"] > 3) &
    (df_filtrado["Horas de Estudo Tradicional"] <= 8)
]


muito_estudo = df_filtrado[
    df_filtrado["Horas de Estudo Tradicional"] > 8
]


# médias

media_pouco_estudo = pouco_estudo["Variação da Nota"].mean()

media_estudo_medio = estudo_medio["Variação da Nota"].mean()

media_muito_estudo = muito_estudo["Variação da Nota"].mean()



# tabela para gráfico

grafico_estudo = pd.DataFrame({

    "Grupo de estudo": [
        "Pouco estudo",
        "Estudo médio",
        "Muito estudo"
    ],

    "Variação média da nota": [
        media_pouco_estudo,
        media_estudo_medio,
        media_muito_estudo
    ]

})


st.dataframe(grafico_estudo)


st.bar_chart(
    grafico_estudo,
    x="Grupo de estudo",
    y="Variação média da nota"
)
# =====================================
# PRINCIPAIS USOS DA IA
# =====================================

st.header("🤖 Principais usos da Inteligência Artificial")


# contando os usos

uso_ia = df_filtrado["Principal Uso IA"].value_counts()


# tabela

st.subheader("Quantidade de estudantes por uso da IA")

st.dataframe(uso_ia)



# gráfico

st.subheader("Distribuição dos usos da IA")


st.bar_chart(uso_ia)
# =====================================
# MÉDIA DA NOTA POR USO DE IA
# =====================================

st.header("📈 Média da nota final por nível de uso da IA")


# criando grupos

ate_3_horas = df_filtrado[
    df_filtrado["Horas Semanais Usando IA"] <= 3
]


de_3_a_8_horas = df_filtrado[
    (df_filtrado["Horas Semanais Usando IA"] > 3) &
    (df_filtrado["Horas Semanais Usando IA"] <= 8)
]


mais_de_8_horas = df_filtrado[
    df_filtrado["Horas Semanais Usando IA"] > 8
]



# calculando médias

nota_ate_3 = ate_3_horas[
    "Nota Depois do Semestre"
].mean()


nota_3_a_8 = de_3_a_8_horas[
    "Nota Depois do Semestre"
].mean()


nota_mais_8 = mais_de_8_horas[
    "Nota Depois do Semestre"
].mean()



# criando tabela para o gráfico

grafico_nota_ia = pd.DataFrame({

    "Uso semanal de IA": [
        "Até 3 horas",
        "3 a 8 horas",
        "Mais de 8 horas"
    ],

    "Média da nota final": [
        nota_ate_3,
        nota_3_a_8,
        nota_mais_8
    ]

})


st.dataframe(grafico_nota_ia)


# gráfico

st.line_chart(
    grafico_nota_ia,
    x="Uso semanal de IA",
    y="Média da nota final"
)
# =====================================
# ABAS DO APLICATIVO
# =====================================

aba1, aba2, aba3, aba4 = st.tabs([
    "🏠 Visão Geral",
    "📊 Análises",
    "📋 Dados",
    "📑 Conclusões"
])
