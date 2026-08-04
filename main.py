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
