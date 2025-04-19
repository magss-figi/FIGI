
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="FIGI – Dashboard de Investimentos")

# Sidebar filters
st.sidebar.header("Filtros")
municipio = st.sidebar.selectbox("Município", ["Belmonte", "Sabugal", "Covilhã"])
polo = st.sidebar.selectbox("Polo", ["Centro", "Sul", "Norte"])
ano = st.sidebar.selectbox("Ano", [2024, 2025, 2026, 2027, 2028])

st.title("FIGI – Plataforma de Gestão de Investimentos")
st.markdown("### Indicadores-Chave (KPI)")

# KPIs mock
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Execução Física", "62%", "🔼 4%")
col2.metric("Execução Orçamental", "58%", "🔽 2%")
col3.metric("Desvio Orçamental", "8%", "🔼 1%")
col4.metric("Redundância", "3.00", "")
col5.metric("Avaliação Estrutural", "5.00", "✅")

st.markdown("---")
st.subheader("Evolução da Execução")

# Fake chart
st.line_chart({
    "Execução Física (%)": np.random.randint(40, 70, 5),
    "Execução Orçamental (%)": np.random.randint(35, 65, 5)
})

st.markdown("---")
st.subheader("Localização do Investimento")
st.map(pd.DataFrame({
    'lat': [40.1829],
    'lon': [-7.3433]
}))

st.markdown("---")
st.subheader("Sumário Técnico")
st.markdown("""
**Projeto:** Beneficiação do Reservatório de Santo Antão  
**Localização:** Belmonte  
**Período:** 2024–2027  
**Investimento Total:** €1.620.950  
**Objetivo:** Aumentar capacidade de reserva e fiabilidade do sistema.
""")

st.markdown("---")
st.subheader("Chat com o THEO")
st.text_input("Faça uma pergunta ao THEO (ex: Qual o investimento com maior risco?)")
