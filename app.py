
import streamlit as st

# Aplicar o tema personalizado
with open("singularis_theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Conteúdo do dashboard
st.title("FIGI - Monitorização de Investimentos")

st.header("Indicadores-Chave de Desempenho")
col1, col2, col3 = st.columns(3)
col1.metric("Execução Física", "36%", "-2%")
col2.metric("Reabilitação", "3.7 km", "+0.2 km")
col3.metric("Sobrecusto", "0%", "0%")

st.header("Resumo Técnico")
st.write("Substituição de aproximadamente 7.200 metros de condutas de água no centro da cidade, com melhoria na fiabilidade e na redução de perdas de água.")

st.header("Interação com THEO")
st.text_input("Pergunta ao assistente THEO:", placeholder="Ex: Quais os projetos com maior risco este ano?")

st.button("Submeter")
