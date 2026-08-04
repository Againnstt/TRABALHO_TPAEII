import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Impacto da IA",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# TÍTULO
# ==========================================

st.title("🤖 Impacto da Inteligência Artificial no Desempenho Acadêmico")

st.header("Projeto de Programação em Python")

st.markdown("""
Este aplicativo apresenta uma análise do impacto do uso da Inteligência Artificial
sobre o desempenho acadêmico dos estudantes.

Os dados utilizados possuem **50.000 estudantes** e **16 variáveis**.
""")
